"""Icon and styling utilities for OctoGreen"""

# Icon mappings using Unicode symbols
ICONS = {
    "download": "⬇️",
    "upload": "📤",
    "chart": "📊",
    "data": "📈",
    "settings": "⚙️",
    "check": "✅",
    "error": "❌",
    "info": "ℹ️",
    "warning": "⚠️",
    "arrow": "→",
    "click": "👆",
    "energy": "⚡",
    "carbon": "🌍",
    "home": "🏠",
    "database": "🗄️",
    "world": "🌐",
    "bank": "🏦",
    "chart_line": "📉",
    "filter": "🔍",
    "save": "💾",
    "report": "📄",
    "success": "🎉",
}

# Minimal Streamlit custom CSS
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500&display=swap');

h1, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
}

body, .stMarkdown {
    font-family: 'Inter', sans-serif !important;
}

.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 6px !important;
    background-color: #10b981 !important;
    color: white !important;
    border: none !important;
}

.stButton > button:hover {
    background-color: #059669 !important;
}
</style>
"""

def get_icon(name):
    """Get icon by name"""
    return ICONS.get(name, "•")

def format_metric(label, value, icon=None):
    """Format a metric with icon"""
    icon_str = f"{icon} " if icon else ""
    return f"{icon_str}{label}: {value}"
