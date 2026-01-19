import streamlit as st
import plotly.express as px
import pandas as pd
from modules import translations

def t(key):
    """Translation helper"""
    return translations.get_text(key, st.session_state.get('language', 'en'))

def download_buttons(df, analysis):
    # Only CSV download for cleaner UX and to prevent auto-trigger issues
    st.download_button(
        f"⬇️ {t('download_csv')}", 
        df.to_csv(index=False), 
        file_name="data.csv", 
        use_container_width=True, 
        key="btn_download_csv"
    )

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
        )
    )
    
    
    def format_number(num):
        """Format large numbers with K/M suffixes"""
        if abs(num) >= 1_000_000:
            return f"{num/1_000_000:.1f}M"
        elif abs(num) >= 1_000:
            return f"{num/1_000:.1f}K"
        else:
            return f"{num:.1f}"
    
    # Enhanced Summary Metrics with new additions
    st.markdown(f"""
        <div style='margin-top: 2rem; margin-bottom: 1.5rem;'>
            <h3 style='color: #1d1d1f; font-size: 1.5rem; font-weight: 600; 
                       border-left: 4px solid #0071e3; padding-left: 1rem;
                       font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;'>
                <i class='fa-solid fa-chart-line' style='color: #0071e3;'></i> {t('performance_insights')}
            </h3>
            <p style='color: #86868b; margin-left: 1.5rem; margin-top: 0.5rem; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;'>{t('key_metrics')}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Add enhanced metric card CSS
    st.markdown("""
        <style>
        .metric-card {
            background: white;
            border: 1px solid #f1f5f9;
            border-radius: 16px;
            padding: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            height: 100%;
            position: relative;
            overflow: hidden;
        }
        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: #e2e8f0;
            transition: all 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
            border-color: #e2e8f0;
        }
        .metric-icon-box {
            width: 52px;
            height: 52px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            flex-shrink: 0;
        }
        .metric-content {
            flex-grow: 1;
        }
        .metric-value {
            font-size: 1.75rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.2;
            letter-spacing: -0.02em;
        }
        .metric-label {
            font-size: 0.9rem;
            color: #64748b;
            font-weight: 500;
            margin-top: 0.2rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        .tooltip-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #e2e8f0;
            color: #64748b;
            font-size: 10px;
            cursor: help;
            position: relative;
        }
        .tooltip-icon:hover::after {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 150%;
            left: 50%;
            transform: translateX(-50%);
            background: #1e293b;
            color: white;
            padding: 0.5rem 0.75rem;
            border-radius: 8px;
            font-size: 0.75rem;
            white-space: normal;
            width: max-content;
            max-width: 200px;
            text-align: center;
            z-index: 1000;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            pointer-events: none;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # First row - Primary Savings metrics
    col1, col2, col3 = st.columns(3, gap="medium")
    
    savings_kwh = analysis['summary']['tasarruf_kwh']
    savings_carbon = analysis['summary']['tasarruf_carbon']
    savings_usd = analysis['summary']['tasarruf_tl']
    
    with col1:
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid #10b981;'>
            <div class='metric-icon-box' style='background: #ecfdf5; color: #10b981;'>
                <i class='fa-solid fa-bolt'></i>
            </div>
            <div class='metric-content'>
                <div class='metric-value'>{format_number(savings_kwh)}</div>
                <div class='metric-label'>
                    {t('energy_savings')}
                    <span class='tooltip-icon' data-tooltip='{t("tooltip_energy_savings")}'>?</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid #059669;'>
            <div class='metric-icon-box' style='background: #f0fdf4; color: #059669;'>
                <i class='fa-solid fa-leaf'></i>
            </div>
            <div class='metric-content'>
                <div class='metric-value'>{format_number(savings_carbon)}</div>
                <div class='metric-label'>
                    {t('carbon_reduction')}
                    <span class='tooltip-icon' data-tooltip='{t("tooltip_carbon_reduction")}'>?</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid #3b82f6;'>
            <div class='metric-icon-box' style='background: #eff6ff; color: #3b82f6;'>
                <i class='fa-solid fa-dollar-sign'></i>
            </div>
            <div class='metric-content'>
                <div class='metric-value'>${format_number(savings_usd)}</div>
                <div class='metric-label'>
                    {t('cost_savings')}
                    <span class='tooltip-icon' data-tooltip='{t("tooltip_cost_savings")}'>?</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Second row - Operational Metrics
    col4, col5, col6, col7 = st.columns(4, gap="medium")
    
    # Calculate additional metrics
    total_consumption = df['consumption_kWh'].sum()
    avg_consumption = df['consumption_kWh'].mean()
    max_consumption = df['consumption_kWh'].max()
    efficiency_score = min(100, (1 - (avg_consumption / max_consumption)) * 100) if max_consumption > 0 else 0
    
    with col4:
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid #6366f1;'>
            <div class='metric-icon-box' style='background: #eef2ff; color: #6366f1;'>
                <i class='fa-solid fa-database'></i>
            </div>
            <div class='metric-content'>
                <div class='metric-value'>{format_number(total_consumption)}</div>
                <div class='metric-label'>
                    {t('total_usage')}
                    <span class='tooltip-icon' data-tooltip='{t("tooltip_total_usage")}'>?</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        
    with col5:
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid #8b5cf6;'>
            <div class='metric-icon-box' style='background: #f5f3ff; color: #8b5cf6;'>
                <i class='fa-solid fa-chart-line'></i>
            </div>
            <div class='metric-content'>
                <div class='metric-value'>{format_number(avg_consumption)}</div>
                <div class='metric-label'>
                    {t('average')}
                    <span class='tooltip-icon' data-tooltip='{t("tooltip_average")}'>?</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        
    with col6:
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid #f59e0b;'>
            <div class='metric-icon-box' style='background: #fffbeb; color: #f59e0b;'>
                <i class='fa-solid fa-triangle-exclamation'></i>
            </div>
            <div class='metric-content'>
                <div class='metric-value'>{format_number(max_consumption)}</div>
                <div class='metric-label'>
                    {t('peak_load')}
                    <span class='tooltip-icon' data-tooltip='{t("tooltip_peak_load")}'>?</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        
    with col7:
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid #14b8a6;'>
            <div class='metric-icon-box' style='background: #f0fdfa; color: #14b8a6;'>
                <i class='fa-solid fa-gauge-high'></i>
            </div>
            <div class='metric-content'>
                <div class='metric-value'>{efficiency_score:.0f}%</div>
                <div class='metric-label'>
                    {t('efficiency_score')}
                    <span class='tooltip-icon' data-tooltip='{t("tooltip_efficiency_score")}'>?</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)



    
    # ========== SAVINGS OPPORTUNITIES SECTION ==========
    st.markdown(f"""
        <div style='margin-top: 3rem; margin-bottom: 1.5rem;'>
            <h3 style='color: #1d1d1f; font-size: 1.5rem; font-weight: 600; 
                       border-left: 4px solid #10b981; padding-left: 1rem;
                       font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;'>
                <i class='fa-solid fa-lightbulb' style='color: #10b981;'></i> {t('savings_opportunities')}
            </h3>
            <p style='color: #86868b; margin-left: 1.5rem; margin-top: 0.5rem; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;'>{t('savings_opportunities_desc')}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Scenario cards CSS
    st.markdown("""
        <style>
        .scenario-card {
            background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
            border: 2px solid #d1fae5;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(16, 185, 129, 0.1);
        }
        .scenario-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(16, 185, 129, 0.2);
            border-color: #10b981;
        }
        .scenario-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #065f46;
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .scenario-icon {
            font-size: 1.3rem;
        }
        .scenario-metrics {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.8rem;
            margin: 1rem 0;
        }
        .scenario-metric {
            text-align: center;
            padding: 0.6rem;
            background: white;
            border-radius: 8px;
            border: 1px solid #d1fae5;
        }
        .scenario-metric-value {
            font-size: 1.3rem;
            font-weight: 700;
            color: #10b981;
        }
        .scenario-metric-label {
            font-size: 0.75rem;
            color: #6b7280;
            margin-top: 0.2rem;
        }
        .scenario-impact {
            background: #ecfdf5;
            border-radius: 8px;
            padding: 0.8rem;
            margin-top: 0.8rem;
        }
        .scenario-impact-title {
            font-size: 0.85rem;
            font-weight: 600;
            color: #065f46;
            margin-bottom: 0.5rem;
        }
        .scenario-impact-items {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .scenario-impact-item {
            font-size: 0.8rem;
            color: #047857;
            background: white;
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            border: 1px solid #a7f3d0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Get current language
    lang = st.session_state.get('language', 'en')
    
    # Display scenarios in grid
    scenarios = analysis.get('scenarios', [])
    
    # FontAwesome icons for different scenarios (replacing emojis)
    fa_icons = [
        '<i class="fa-solid fa-bolt" style="color: #f59e0b;"></i>',
        '<i class="fa-solid fa-moon" style="color: #8b5cf6;"></i>',
        '<i class="fa-solid fa-chart-line" style="color: #3b82f6;"></i>',
        '<i class="fa-solid fa-calendar-check" style="color: #10b981;"></i>',
        '<i class="fa-solid fa-wrench" style="color: #ef4444;"></i>',
        '<i class="fa-solid fa-bullseye" style="color: #06b6d4;"></i>'
    ]
    
    # Show scenarios in pairs
    for i in range(0, len(scenarios), 2):
        cols = st.columns(2)
        
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(scenarios):
                scenario = scenarios[idx]
                
                # Select title based on language
                title = scenario['title_tr'] if lang == 'tr' else scenario['title_en']
                
                # Get FontAwesome icon
                icon = fa_icons[idx] if idx < len(fa_icons) else '<i class="fa-solid fa-lightbulb" style="color: #f59e0b;"></i>'
                
                with col:
                    # Format values safely - ensure reasonable display
                    kwh_val = format_number(scenario['kwh'])
                    carbon_val = format_number(scenario['carbon'])
                    cost_val = format_number(scenario['cost'])
                    trees_val = int(min(scenario['trees'], 999999)) if scenario['trees'] < 1e15 else 0
                    homes_val = int(min(scenario['homes'], 999999)) if scenario['homes'] < 1e15 else 0
                    cars_val = int(min(scenario['cars'], 999999)) if scenario['cars'] < 1e15 else 0
                    
                    # Compact card design - prevents overflow
                    st.markdown(f'''<div style="background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 1.25rem; margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.04); overflow: hidden;">
<div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
<div style="width: 40px; height: 40px; min-width: 40px; background: linear-gradient(135deg, #ecfdf5, #d1fae5); border-radius: 10px; display: flex; align-items: center; justify-content: center;">{icon}</div>
<div style="font-size: 0.95rem; font-weight: 600; color: #1e293b; line-height: 1.3; overflow: hidden; text-overflow: ellipsis;">{title}</div>
</div>
<div style="display: flex; gap: 0.5rem; margin-bottom: 1rem; flex-wrap: wrap;">
<div style="flex: 1; min-width: 70px; text-align: center; padding: 0.75rem 0.5rem; background: #f0fdf4; border-radius: 10px;">
<div style="font-size: 1.1rem; font-weight: 700; color: #059669; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{kwh_val}</div>
<div style="font-size: 0.65rem; color: #6b7280; text-transform: uppercase; margin-top: 0.2rem;">kWh</div>
</div>
<div style="flex: 1; min-width: 70px; text-align: center; padding: 0.75rem 0.5rem; background: #ecfeff; border-radius: 10px;">
<div style="font-size: 1.1rem; font-weight: 700; color: #0891b2; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{carbon_val}</div>
<div style="font-size: 0.65rem; color: #6b7280; text-transform: uppercase; margin-top: 0.2rem;">kg CO₂</div>
</div>
<div style="flex: 1; min-width: 70px; text-align: center; padding: 0.75rem 0.5rem; background: #f0f9ff; border-radius: 10px;">
<div style="font-size: 1.1rem; font-weight: 700; color: #0284c7; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${cost_val}</div>
<div style="font-size: 0.65rem; color: #6b7280; text-transform: uppercase; margin-top: 0.2rem;">USD</div>
</div>
</div>
<div style="background: #f8fafc; border-radius: 10px; padding: 0.75rem;">
<div style="font-size: 0.75rem; font-weight: 600; color: #065f46; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.4rem;">
<i class="fa-solid fa-earth-americas" style="color: #10b981;"></i> {t("global_impact")}
</div>
<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
<span style="font-size: 0.7rem; color: #047857; background: white; padding: 0.35rem 0.5rem; border-radius: 6px; border: 1px solid #d1fae5; display: inline-flex; align-items: center; gap: 0.3rem;">
<i class="fa-solid fa-tree" style="color: #22c55e;"></i> {trees_val}
</span>
<span style="font-size: 0.7rem; color: #047857; background: white; padding: 0.35rem 0.5rem; border-radius: 6px; border: 1px solid #d1fae5; display: inline-flex; align-items: center; gap: 0.3rem;">
<i class="fa-solid fa-house" style="color: #f59e0b;"></i> {homes_val}
</span>
<span style="font-size: 0.7rem; color: #047857; background: white; padding: 0.35rem 0.5rem; border-radius: 6px; border: 1px solid #d1fae5; display: inline-flex; align-items: center; gap: 0.3rem;">
<i class="fa-solid fa-car" style="color: #ef4444;"></i> {cars_val}
</span>
</div>
</div>
</div>''', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(f"""
        <div style='margin-top: 3rem; margin-bottom: 1rem;'>
            <h3 style='color: #1d1d1f; font-size: 1.5rem; font-weight: 600; 
                       border-left: 4px solid #0071e3; padding-left: 1rem;'>
                <i class='fa-solid fa-chart-area' style='color: #0071e3;'></i> {t('consumption_timeline')}
            </h3>
            <p style='color: #86868b; margin-left: 1.5rem; margin-top: 0.5rem; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;'>
                {t('realtime_usage')}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    fig = px.line(df, x='timestamp', y='consumption_kWh', color='device_id')
    fig.update_layout(
        **common_layout,
        xaxis_title=t('time'),
        yaxis_title=t('consumption_kwh'),
        legend_title=t('device_id'),
        legend=dict(
            bgcolor='white',
            bordercolor=grid_color,
            borderwidth=1
        ),
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Create 2-column grid for Daily & Hourly plots
    col_grid1, col_grid2 = st.columns(2, gap="medium")
    
    with col_grid1:
        # Daily Aggregation
        st.markdown(f"""
            <div style='margin-top: 1rem; margin-bottom: 1rem;'>
                <h3 style='color: #1d1d1f; font-size: 1.3rem; font-weight: 600; 
                           border-left: 4px solid #10b981; padding-left: 1rem;
                           font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;'>
                    <i class='fa-solid fa-calendar-days' style='color: #10b981;'></i> {t('daily_energy_profile')}
                </h3>
                <p style='color: #86868b; margin-left: 1.5rem; margin-top: 0.5rem; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;'>
                    {t('total_consumption_day')}
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        daily = analysis['summary']['daily_total']
        fig2 = px.bar(x=list(daily.keys()), y=list(daily.values()), 
                     labels={'x':t('day'), 'y':t('total_kwh')})
        fig2.update_layout(
            **common_layout,
            xaxis_title=t('day'),
            yaxis_title=t('total_kwh'),
            showlegend=False,
            height=350,
            margin=dict(t=20, b=0, l=0, r=0)
        )
        fig2.update_traces(
            marker_color='#10b981',
            marker_line_color='#0d8f6e',
            marker_line_width=1.5,
            opacity=0.8
        )
        st.plotly_chart(fig2, use_container_width=True)
        
    with col_grid2:
        # Hourly Pattern Analysis
        st.markdown(f"""
            <div style='margin-top: 1rem; margin-bottom: 1rem;'>
                <h3 style='color: #1d1d1f; font-size: 1.3rem; font-weight: 600; 
                           border-left: 4px solid #3b82f6; padding-left: 1rem;
                           font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;'>
                    <i class='fa-solid fa-clock' style='color: #3b82f6;'></i> {t('hourly_usage_patterns')}
                </h3>
                <p style='color: #86868b; margin-left: 1.5rem; margin-top: 0.5rem; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;'>
                    {t('average_by_hour')}
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        hourly = analysis['summary']['hourly_avg']
        fig3 = px.bar(x=list(hourly.keys()), y=list(hourly.values()), 
                     labels={'x':t('hour'), 'y':t('average_kwh')})
        fig3.update_layout(
            **common_layout,
            xaxis_title=t('hour'),
            yaxis_title=t('average_kwh'),
            showlegend=False,
            height=350,
            margin=dict(t=20, b=0, l=0, r=0)
        )
        fig3.update_traces(
            marker_color='#3b82f6',
            marker_line_color='#2563eb',
            marker_line_width=1.5,
            opacity=0.8
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    # Anomaly Detection
    st.markdown(f"""
        <div style='margin-top: 3rem; margin-bottom: 1rem;'>
            <h3 style='color: #1d1d1f; font-size: 1.5rem; font-weight: 600; 
                       border-left: 4px solid #ef4444; padding-left: 1rem;'>
                <i class='fa-solid fa-magnifying-glass-chart' style='color: #ef4444;'></i> {t('anomaly_detection')}
            </h3>
            <p style='color: #86868b; margin-left: 1.5rem; margin-top: 0.5rem; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;'>
                {t('unusual_patterns')}
            </p>
        </div>
    """, unsafe_allow_html=True)
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
            xaxis_title=t('time'),
            yaxis_title=t('consumption_kwh'),
            legend=dict(
                bgcolor='white',
                bordercolor=grid_color,
                borderwidth=1
            )
        )
        
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info(t("no_anomalies"))

@st.cache_data
def generate_pdf_report(df, analysis):
    from fpdf import FPDF
    
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
    
    # Use dest='S' to return PDF as bytes string
    pdf_string = pdf.output(dest='S')
    
    # Convert to bytes if it's a string (for fpdf compatibility)
    if isinstance(pdf_string, str):
        return pdf_string.encode('latin-1')
    return pdf_string

