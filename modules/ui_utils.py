"""Icon and styling utilities for OctoGreen"""

# White theme CSS with better typography and loading
CUSTOM_CSS = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600&display=swap');

/* Global white theme */
.stApp {
    background-color: white !important;
}

.main .block-container {
    background-color: white !important;
}

/* Date input text color */
.stDateInput input {
    color: #1f2937 !important;
}

.stDateInput input::placeholder {
    color: #9ca3af !important;
}

/* Typography */
h1 {
    font-family: "Poppins", sans-serif !important;
    font-weight: 700 !important;
    font-size: 3rem !important;
    color: #10b981 !important;
}

h2, h3, h4, h5, h6 {
    font-family: "Poppins", sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.8rem !important;
    margin-top: 2rem !important;
    color: #1f2937 !important;
}

/* Sidebar white theme */
.stSidebar {
    background-color: white !important;
    border-right: 1px solid #e5e7eb !important;
}

.stSidebar > div {
    background-color: white !important;
}

.stSidebar .stRadio > label {
    font-size: 1.3rem !important;
    font-weight: 500 !important;
    color: #374151 !important;
}

.stSidebar .stSelectbox > label {
    font-size: 1.3rem !important;
    font-weight: 500 !important;
    color: #374151 !important;
}

.stSidebar .stFileUploader > label {
    font-size: 1.3rem !important;
    font-weight: 500 !important;
    color: #374151 !important;
}

.stSidebar .stDateInput > label {
    font-size: 1.3rem !important;
    font-weight: 500 !important;
    color: #374151 !important;
}

.stSidebar h1, .stSidebar h2, .stSidebar h3 {
    font-size: 1.6rem !important;
    color: #10b981 !important;
}

.stSidebar h4 {
    font-size: 1.4rem !important;
    color: #374151 !important;
}

/* Sidebar radio button styling */
.stSidebar .stRadio > div {
    background-color: white !important;
}

.stSidebar .stRadio > div > label {
    background-color: white !important;
    color: #1f2937 !important;
    font-size: 1.4rem !important;
    font-weight: 600 !important;
    padding: 1rem 1.5rem !important;
    border-radius: 8px !important;
    border: 2px solid #e5e7eb !important;
    margin: 0.5rem 0 !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
}

.stSidebar .stRadio > div > label:hover {
    border-color: #10b981 !important;
    background-color: #f0fdf4 !important;
}

.stSidebar .stRadio > div > label > div {
    color: #1f2937 !important;
    font-weight: 600 !important;
}

.stSidebar .stRadio > div > label > div > p {
    color: #1f2937 !important;
    font-weight: 600 !important;
    margin: 0 !important;
}

.stSidebar .stRadio [data-checked="true"] {
    background-color: #10b981 !important;
    color: white !important;
    border-color: #10b981 !important;
}

.stSidebar .stRadio [data-checked="true"] > div {
    color: white !important;
}

.stSidebar .stRadio [data-checked="true"] > div > p {
    color: white !important;
}

/* Sidebar selectbox styling */
.stSidebar .stSelectbox > div > div {
    background-color: white !important;
    border: 2px solid #e5e7eb !important;
    border-radius: 8px !important;
    font-size: 1.3rem !important;
    color: #1f2937 !important;
}

.stSidebar .stSelectbox option {
    color: #1f2937 !important;
    font-size: 1.3rem !important;
}

/* Selectbox dropdown menu - force white theme */
[data-baseweb="select"] {
    background-color: white !important;
}

[data-baseweb="popover"] {
    background-color: white !important;
}

[data-baseweb="menu"] {
    background-color: white !important;
}

[role="listbox"] {
    background-color: white !important;
    border: 1px solid #e5e7eb !important;
}

[role="option"] {
    background-color: white !important;
    color: #1f2937 !important;
    font-size: 1.3rem !important;
    padding: 0.75rem 1rem !important;
}

[role="option"]:hover {
    background-color: #f0fdf4 !important;
    color: #10b981 !important;
}

[data-baseweb="select"] > div {
    background-color: white !important;
    color: #1f2937 !important;
}

.stSidebar .stFileUploader > div {
    background-color: white !important;
    border: 1px solid #d1d5db !important;
    border-radius: 6px !important;
}

/* Button styling */
.stButton > button {
    background-color: #10b981 !important;
    border-radius: 8px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    padding: 0.75rem 1.5rem !important;
    border: none !important;
    color: white !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background-color: #059669 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3) !important;
}

/* Alert styling - white theme */
.stSuccess {
    background-color: #f0fdf4 !important;
    border: 1px solid #10b981 !important;
    border-radius: 8px !important;
    padding: 1rem !important;
    font-size: 1.1rem !important;
    color: #065f46 !important;
}

.stError {
    background-color: #fef2f2 !important;
    border: 1px solid #ef4444 !important;
    border-radius: 8px !important;
    padding: 1rem !important;
    font-size: 1.1rem !important;
    color: #991b1b !important;
}

.stInfo {
    background-color: #eff6ff !important;
    border: 1px solid #3b82f6 !important;
    border-radius: 8px !important;
    padding: 1rem !important;
    font-size: 1.1rem !important;
    color: #1e40af !important;
}

.stWarning {
    background-color: #fffbeb !important;
    border: 1px solid #f59e0b !important;
    border-radius: 8px !important;
    padding: 1rem !important;
    font-size: 1.1rem !important;
    color: #92400e !important;
}

/* Main content white theme */
.main > div {
    background-color: white !important;
}

.block-container {
    background-color: white !important;
    padding-top: 2rem !important;
}

/* Input fields white theme */
.stSelectbox > div > div {
    background-color: white !important;
    border: 1px solid #d1d5db !important;
}

.stTextInput > div > div {
    background-color: white !important;
    border: 1px solid #d1d5db !important;
}

.stDateInput > div > div {
    background-color: white !important;
    border: 1px solid #d1d5db !important;
}

.stFileUploader > div {
    background-color: white !important;
    border: 1px solid #d1d5db !important;
    border-radius: 6px !important;
}

/* General text sizing */
.stMarkdown {
    font-size: 1.3rem !important;
    line-height: 1.6 !important;
    color: #374151 !important;
}

/* Welcome section - white theme */
.welcome-section {
    background: white !important;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    border: 2px solid #10b981;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.welcome-section h2 {
    color: #10b981 !important;
    margin-bottom: 1rem !important;
}

.welcome-section p {
    color: #374151 !important;
    font-size: 1.4rem !important;
    margin: 0 !important;
}

/* Feature cards - white theme */
.feature-card {
    background: white !important;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1rem 0;
    border: 1px solid #e5e7eb;
    border-left: 4px solid #10b981;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    color: #1f2937 !important;
}

.feature-card h3 {
    color: #10b981 !important;
    margin-bottom: 1rem !important;
}

.feature-card ul {
    color: #374151 !important;
}

.feature-card li {
    color: #374151 !important;
    margin-bottom: 0.5rem;
}
</style>
'''

def show_loading_progress(message, steps=None):
    """Show enhanced loading progress"""
    import streamlit as st
    import time
    
    if steps:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, step in enumerate(steps):
            status_text.text(f"• {step}")
            progress_bar.progress((i + 1) / len(steps))
            time.sleep(0.2)  # Further reduced to 0.2 seconds
        
        status_text.text(f"✓ {message}")
        time.sleep(0.1)  # Further reduced to 0.1 seconds
        progress_bar.empty()
        status_text.empty()
        # Don't call st.rerun() here - let the natural flow continue
    else:
        with st.spinner(f"• {message}"):
            time.sleep(0.3)  # Reduced to 0.3 seconds

def show_welcome_screen():
    """Show welcome screen with features"""
    import streamlit as st

    # Title with improved typography and spacing
    st.markdown("""
    <div style='text-align:center; margin: 3rem 0 4rem 0;'>
        <h1 style='color: #10b981; margin: 0; font-size: 3.5rem; letter-spacing: -0.5px; font-weight: 800;'>OctoGreen</h1>
        <div style='height: 8px; width: 80px; background: #10b981; margin: 1rem auto; border-radius: 4px;'></div>
        <h3 style='color: #4b5563; font-weight: 400; letter-spacing: 0.5px; margin-top: 1rem;'>Smart Energy Analysis Platform</h3>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for the feature cards with better spacing
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class='custom-card'>
            <h3>Data Analysis</h3>
            <ul>
                <li>Analyze energy consumption patterns</li>
                <li>View detailed statistics and trends</li>
                <li>Generate comprehensive reports</li>
            </ul>
        </div>
        
        <div class='custom-card'>
            <h3>Multiple Data Sources</h3>
            <ul>
                <li>Connect to various open data sources</li>
                <li>Upload your own CSV files</li>
                <li>Real-time data integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='custom-card'>
            <h3>AI-Powered Insights</h3>
            <ul>
                <li>Get smart recommendations</li>
                <li>Predict future consumption</li>
                <li>Identify saving opportunities</li>
            </ul>
        </div>
        
        <div class='custom-card'>
            <h3>User Experience</h3>
            <ul>
                <li>Intuitive controls</li>
                <li>Interactive visualizations</li>
                <li>Responsive design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # Add a getting started section with improved typography
    st.markdown("""
    <div style='max-width: 800px; margin: 0 auto;'>
        <h3 style='color: #1e293b; font-weight: 600; margin-bottom: 1.5rem; border-bottom: 2px solid #e5e7eb; padding-bottom: 0.5rem;'>Getting Started</h3>
        <div style='display: flex; justify-content: space-between; margin-top: 2rem;'>
            <div style='flex: 1; text-align: center; padding: 0 1rem;'>
                <div style='background: #e0f2fe; color: #0369a1; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-weight: 700;'>1</div>
                <p style='font-weight: 500; color: #1e293b;'>Select your data source from the sidebar</p>
            </div>
            <div style='flex: 1; text-align: center; padding: 0 1rem;'>
                <div style='background: #dbeafe; color: #1d4ed8; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-weight: 700;'>2</div>
                <p style='font-weight: 500; color: #1e293b;'>Choose your date range and parameters</p>
            </div>
            <div style='flex: 1; text-align: center; padding: 0 1rem;'>
                <div style='background: #dcfce7; color: #166534; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-weight: 700;'>3</div>
                <p style='font-weight: 500; color: #1e293b;'>Explore the analysis and visualizations</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add the CSS for the welcome screen with improved typography
    welcome_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .custom-card {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 2rem;
        background: #ffffff;
        margin-bottom: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
    }
    
    .custom-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);
        border-color: #d1d5db;
    }
    
    .custom-card h3 {
        color: #111827;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 1.25rem;
        margin: 0 0 1.25rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #f3f4f6;
        letter-spacing: -0.01em;
    }
    
    .custom-card ul {
        margin: 0;
        padding-left: 1.5rem;
        color: #4b5563;
        line-height: 1.75;
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
    }
    
    .custom-card li {
        margin-bottom: 0.5rem;
        position: relative;
    }
    
    .custom-card li:before {
        content: '';
        position: absolute;
        left: -1.25rem;
        top: 0.75em;
        height: 6px;
        width: 6px;
        background-color: #10b981;
        border-radius: 50%;
    }
    </style>
    """
    st.markdown(welcome_css, unsafe_allow_html=True)