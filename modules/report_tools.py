import streamlit as st
import plotly.express as px
import pandas as pd

def download_buttons(df, analysis):
    st.download_button("Download data as CSV", df.to_csv(index=False), file_name="data.csv")
    if st.button("Download PDF report"):
        pdf_bytes = generate_pdf_report(df, analysis)
        st.download_button("Download PDF report (generated)", pdf_bytes, file_name="report.pdf")

def visualize(df, analysis):
    import plotly.graph_objects as go
    st.markdown("### Summary Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Estimated Savings (kWh)", f"{analysis['summary']['tasarruf_kwh']:.2f}")
    col2.metric("Carbon Savings (kg CO2)", f"{analysis['summary']['tasarruf_carbon']:.2f}")
    col3.metric("USD Savings", f"{analysis['summary']['tasarruf_tl']:.2f}")

    st.markdown("### Hourly Consumption (All Devices)")
    fig = px.line(df, x='timestamp', y='consumption_kWh', color='device_id', title='Hourly Consumption')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Daily Total Consumption")
    daily = analysis['summary']['daily_total']
    fig2 = px.bar(x=list(daily.keys()), y=list(daily.values()), labels={'x':'Day', 'y':'Total kWh'}, title='Daily Total Consumption')
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Hourly Average Consumption")
    hourly = analysis['summary']['hourly_avg']
    fig3 = px.bar(x=list(hourly.keys()), y=list(hourly.values()), labels={'x':'Hour', 'y':'Average kWh'}, title='Hourly Average Consumption')
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("### Anomaly Points")
    anomalies = analysis['summary']['anomalies']
    if anomalies:
        anom_df = pd.DataFrame(anomalies)
        st.dataframe(anom_df)
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(x=df['timestamp'], y=df['consumption_kWh'], mode='lines', name='Consumption'))
        fig4.add_trace(go.Scatter(x=anom_df['timestamp'], y=anom_df['consumption_kWh'], mode='markers', name='Anomaly', marker=dict(color='red', size=10)))
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No anomalies detected.")

def generate_pdf_report(df, analysis):
    from fpdf import FPDF
    import io
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="OctoGreen Energy Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Estimated Savings: {analysis['summary']['tasarruf_kwh']:.2f} kWh", ln=True)
    pdf.cell(200, 10, txt=f"Carbon Savings: {analysis['summary']['tasarruf_carbon']:.2f} kg CO2", ln=True)
    pdf.cell(200, 10, txt=f"USD Savings: {analysis['summary']['tasarruf_tl']:.2f}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Recommendations:", ln=True)
    for rec in analysis['recommendations']:
        pdf.multi_cell(0, 10, rec)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Daily Totals:", ln=True)
    for day, val in analysis['summary']['daily_total'].items():
        pdf.cell(200, 10, txt=f"{day}: {val:.2f} kWh", ln=True)
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()
