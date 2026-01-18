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
    
    # Set the default theme for all plots
    plot_bgcolor = 'rgba(0,0,0,0)'
    paper_bgcolor = 'rgba(0,0,0,0)'
    font_color = '#1f2937'
    grid_color = '#e5e7eb'
    
    # Common layout for all figures
    common_layout = dict(
        plot_bgcolor=plot_bgcolor,
        paper_bgcolor=paper_bgcolor,
        font=dict(color=font_color, family='Inter, sans-serif'),
        xaxis=dict(
            showgrid=True,
            gridcolor=grid_color,
            gridwidth=1,
            linecolor=grid_color,
            linewidth=1,
            showline=True,
            mirror=True
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=grid_color,
            gridwidth=1,
            linecolor=grid_color,
            linewidth=1,
            showline=True,
            mirror=True
        ),
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    # Summary Metrics
    st.markdown("<h3 style='color:#1f2937; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.5rem; margin-top: 2rem;'>Summary Metrics</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-card'>" + 
                    f"<div class='metric-value'>{analysis['summary']['tasarruf_kwh']:.2f}</div>" +
                    "<div class='metric-label'>Estimated Savings (kWh)</div>" +
                    "</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'>" + 
                    f"<div class='metric-value'>{analysis['summary']['tasarruf_carbon']:.2f}</div>" +
                    "<div class='metric-label'>Carbon Savings (kg CO2)</div>" +
                    "</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-card'>" + 
                    f"<div class='metric-value'>{analysis['summary']['tasarruf_tl']:.2f}</div>" +
                    "<div class='metric-label'>USD Savings</div>" +
                    "</div>", unsafe_allow_html=True)
    
    # Hourly Consumption
    st.markdown("<h3 style='color:#1f2937; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.5rem; margin-top: 2rem;'>Hourly Consumption (All Devices)</h3>", unsafe_allow_html=True)
    fig = px.line(df, x='timestamp', y='consumption_kWh', color='device_id')
    fig.update_layout(
        **common_layout,
        xaxis_title='Time',
        yaxis_title='Consumption (kWh)',
        legend_title='Device ID',
        legend=dict(
            bgcolor='white',
            bordercolor=grid_color,
            borderwidth=1
        )
    )
    st.plotly_chart(fig, width="stretch")
    
    # Daily Total Consumption
    st.markdown("<h3 style='color:#1f2937; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.5rem; margin-top: 2rem;'>Daily Total Consumption</h3>", unsafe_allow_html=True)
    daily = analysis['summary']['daily_total']
    fig2 = px.bar(x=list(daily.keys()), y=list(daily.values()), 
                 labels={'x':'Day', 'y':'Total kWh'})
    fig2.update_layout(
        **common_layout,
        xaxis_title='Day',
        yaxis_title='Total Consumption (kWh)',
        showlegend=False
    )
    fig2.update_traces(
        marker_color='#10b981',
        marker_line_color='#0d8f6e',
        marker_line_width=1.5,
        opacity=0.8
    )
    st.plotly_chart(fig2, width="stretch")
    
    # Hourly Average Consumption
    st.markdown("<h3 style='color:#1f2937; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.5rem; margin-top: 2rem;'>Hourly Average Consumption</h3>", unsafe_allow_html=True)
    hourly = analysis['summary']['hourly_avg']
    fig3 = px.bar(x=list(hourly.keys()), y=list(hourly.values()), 
                 labels={'x':'Hour', 'y':'Average kWh'})
    fig3.update_layout(
        **common_layout,
        xaxis_title='Hour of Day',
        yaxis_title='Average Consumption (kWh)',
        showlegend=False
    )
    fig3.update_traces(
        marker_color='#3b82f6',
        marker_line_color='#2563eb',
        marker_line_width=1.5,
        opacity=0.8
    )
    st.plotly_chart(fig3, width="stretch")
    
    # Anomaly Points
    st.markdown("<h3 style='color:#1f2937; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.5rem; margin-top: 2rem;'>Anomaly Detection</h3>", unsafe_allow_html=True)
    anomalies = analysis['summary']['anomalies']
    if anomalies:
        anom_df = pd.DataFrame(anomalies)
        
        # Style the anomalies dataframe
        st.markdown("""
        <style>
            .stDataFrame {
                border: 1px solid #e5e7eb !important;
                border-radius: 8px !important;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
            }
            .stDataFrame th {
                background-color: #f9fafb !important;
                color: #1f2937 !important;
                font-weight: 600 !important;
                border-bottom: 1px solid #e5e7eb !important;
            }
            .stDataFrame td {
                color: #1f2937 !important;
                border-bottom: 1px solid #f3f4f6 !important;
            }
            .stDataFrame tr:hover {
                background-color: #f9fafb !important;
            }
            .metric-card {
                background: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 1.5rem;
                text-align: center;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            }
            .metric-value {
                font-size: 1.8rem;
                font-weight: 700;
                color: #10b981;
                margin-bottom: 0.5rem;
            }
            .metric-label {
                font-size: 0.9rem;
                color: #6b7280;
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Display with Pandas Styler to force light theme
        st.dataframe(
            anom_df.style.set_properties(**{
                'background-color': '#ffffff',
                'color': '#1f2937',
                'border-color': '#e5e7eb'
            }).set_table_styles([
                {'selector': 'th', 'props': [('background-color', '#f9fafb'), ('color', '#1f2937'), ('font-weight', '600')]},
                {'selector': 'td', 'props': [('color', '#1f2937')]}
            ]),
            width="stretch"
        )
        
        # Anomaly plot
        fig4 = go.Figure()
        
        # Main line
        fig4.add_trace(go.Scatter(
            x=df['timestamp'], 
            y=df['consumption_kWh'], 
            mode='lines', 
            name='Consumption',
            line=dict(color='#3b82f6', width=2),
            opacity=0.8
        ))
        
        # Anomaly points
        fig4.add_trace(go.Scatter(
            x=anom_df['timestamp'], 
            y=anom_df['consumption_kWh'], 
            mode='markers', 
            name='Anomaly', 
            marker=dict(
                color='#ef4444',
                size=10,
                line=dict(color='white', width=1)
            )
        ))
        
        fig4.update_layout(
            **common_layout,
            xaxis_title='Time',
            yaxis_title='Consumption (kWh)',
            legend=dict(
                bgcolor='white',
                bordercolor=grid_color,
                borderwidth=1
            )
        )
        
        st.plotly_chart(fig4, width="stretch")
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
