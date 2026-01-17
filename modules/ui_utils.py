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
            time.sleep(0.5)
        
        status_text.text(f"✓ {message}")
        time.sleep(0.5)
        progress_bar.empty()
        status_text.empty()
    else:
        with st.spinner(f"• {message}"):
            time.sleep(1)

def show_welcome_screen():
    """Show welcome screen with features"""
    import streamlit as st
    
    # Title centered
    st.markdown("<h1 style='text-align:center;margin:2rem 0;'>OctoGreen: Smart Energy Analysis Platform</h1>", unsafe_allow_html=True)
    CUSTOM_CSS = """
    .custom-card {
         border: none;
         border-radius: 18px;
         padding: 1.7rem 1.7rem 1.3rem 1.7rem;
         background: #f7f8fa;
         margin-bottom: 1.7rem;
         box-shadow: 0 4px 18px rgba(30,41,59,0.10);
         transition: box-shadow 0.2s;
    }
    .custom-card:hover {
         box-shadow: 0 8px 32px rgba(30,41,59,0.16);
    }
    .custom-card h3 {
         color: #1e293b;
         font-weight: 700;
         margin-bottom: 1rem;
         letter-spacing: 0.01em;
    }
    .custom-card ul {
         margin-left: 1.2rem;
         color: #334155;
         font-size: 1.08rem;
    }
