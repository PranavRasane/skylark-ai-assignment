# app.py - MAIN ENTRY POINT (FINAL POLISHED VERSION)
import streamlit as st
import importlib.util
import sys
import os

# Page configuration
st.set_page_config(
    page_title="Skylark Brief: AI-Powered Drone Intelligence",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/PranavRasane',
        'Report a bug': None,
        'About': "AI Engineering Assignment - Transforming Drone Data into Confident Decisions"
    }
)

# ====== UPDATED CSS SECTION - FIXED PAGE SCROLLING ======
st.markdown("""
<style>
    /* ====== CRITICAL FIX: Remove ALL white bars/spacing ====== */
    
    /* Target the main content area */
    .stApp {
        padding: 0 !important;
        overflow-anchor: none; /* Prevent scroll anchoring */
    }
    
    /* Remove top and bottom padding from main container */
    .main .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* Remove spacing in Streamlit's vertical layout */
    [data-testid="stVerticalBlock"] {
        gap: 0.5rem !important;
    }
    
    /* Target the section causing white bars */
    div[data-testid="stVerticalBlock"] > div > div > div > div {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* Remove spacing from markdown/text elements */
    div[data-testid="stMarkdownContainer"] {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }
    
    .stMarkdown {
        margin-bottom: 0rem !important;
        padding-bottom: 0rem !important;
        line-height: 1.4 !important;
    }
    
    /* Remove column spacing */
    [data-testid="column"] {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* ====== FIX: Ensure all pages start from top ====== */
    html, body {
        scroll-behavior: auto !important;
    }
    
    /* Hide scrollbar but keep functionality */
    .main .block-container {
        scroll-margin-top: 0 !important;
    }
    
    /* ====== FIXED: Sidebar Alignment ====== */
    
    /* Sidebar container - move content upward */
    .sidebar .sidebar-content {
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Sidebar header - centered and upward */
    .sidebar-header {
        text-align: center !important;
        margin-bottom: 1rem !important;
        padding-bottom: 1rem;
        border-bottom: 1px solid #E5E7EB;
    }
    
    .sidebar-header h2 {
        color: #1E3A8A;
        margin-bottom: 0.3rem !important;
        font-size: 1.8rem !important; /* Larger font */
        line-height: 1.2;
        text-align: center !important;
        font-weight: 700 !important;
    }
    
    .sidebar-header p {
        color: #6B7280;
        font-size: 0.95rem;
        text-align: center !important;
        font-style: italic;
        margin-bottom: 0 !important;
        line-height: 1.3;
    }
    
    /* Navigation section - tighter spacing */
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #1E3A8A !important;
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }
    
    /* Navigation buttons - tighter spacing */
    [data-testid="stSidebar"] .stButton button {
        margin-top: 0.3rem !important;
        margin-bottom: 0.3rem !important;
        padding: 0.6rem 0.8rem !important;
        font-size: 0.9rem !important;
    }
    
    /* Progress section - tighter */
    .progress-section {
        background: #F8FAFC;
        padding: 0.8rem !important;
        border-radius: 8px;
        margin: 0.5rem 0 !important;
    }
    
    .progress-section h3 {
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
        font-size: 1.1rem !important;
    }
    
    /* Creator info - tighter */
    [data-testid="stSidebar"] .stMarkdown p {
        margin-bottom: 0.2rem !important;
        line-height: 1.3;
        font-size: 0.85rem;
    }
    
    /* Remove extra spacing in sidebar */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.3rem !important;
    }
    
    /* ====== Your existing styles (minimized spacing) ====== */
    
    .main-header {
        font-size: 2.8rem;
        color: #1E3A8A;
        font-weight: 800;
        margin-bottom: 0.5rem !important;
        padding-top: 0.5rem;
        text-align: center;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #6B7280;
        font-weight: 400;
        margin-bottom: 0.5rem !important;
        text-align: center;
        font-style: italic;
        line-height: 1.4;
    }
    
    /* Page-specific headers */
    .page-header {
        color: #1E3A8A;
        font-size: 2.2rem;
        font-weight: 700;
        margin-top: 0.5rem !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #3B82F6;
        text-align: center;
    }
    
    /* ====== NEW: White Background Box for Hero Section ====== */
    .white-box-container {
        background: white !important;
        padding: 2.5rem !important;
        border-radius: 16px !important;
        margin: 0.5rem 0 1rem 0 !important; /* Reduced bottom margin */
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08) !important;
        border: 1px solid #E5E7EB !important;
    }
    
    .hero-title-box {
        color: #1E40AF;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.2rem !important;
        line-height: 1.3;
        padding-bottom: 0.8rem;
        border-bottom: 2px solid #E5E7EB;
    }
    
    .hero-text-box {
        color: #4B5563;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 1.2rem !important;
        padding: 0.5rem 0;
    }
    
    .hero-highlight {
        color: #1E40AF;
        font-weight: 600;
        background: linear-gradient(120deg, #DBEAFE 0%, #DBEAFE 100%);
        background-repeat: no-repeat;
        background-size: 100% 0.4em;
        background-position: 0 88%;
        padding: 0 0.2rem;
    }
    
    /* ====== FIX: Navigation Section Title Alignment ====== */
    .section-title-container {
        margin-top: 0.5rem !important;
        margin-bottom: 0.8rem !important;
    }
    
    .section-title {
        color: #1F2937;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem !important;
        padding-bottom: 0.3rem;
        border-bottom: 2px solid #E5E7EB;
        line-height: 1.2;
    }
    
    .section-subtitle {
        color: #6B7280;
        font-size: 1rem;
        margin-bottom: 0.8rem !important;
        line-height: 1.4;
    }
    
    /* Cards - minimal bottom spacing */
    .card {
        background: white;
        border-radius: 12px;
        padding: 1.2rem !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 0.5rem !important;
        border: 1px solid #E5E7EB;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
        border-color: #3B82F6;
    }
    
    .card h3 {
        color: #1E40AF;
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
        font-size: 1.3rem;
        min-height: 3.2rem;
        line-height: 1.3;
    }
    
    .card p {
        color: #4B5563;
        flex-grow: 1;
        line-height: 1.5;
        margin-bottom: 0.8rem !important;
        font-size: 0.95rem;
    }
    
    .card-featured {
        border: 2px solid #3B82F6;
        background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(90deg, #3B82F6, #2563EB);
        color: white;
        border: none;
        padding: 0.7rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: auto;
    }
    
    .stButton button:hover {
        background: linear-gradient(90deg, #2563EB, #1D4ED8);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(37, 99, 235, 0.25);
    }
    
    .stButton button[kind="secondary"] {
        background: linear-gradient(90deg, #6B7280, #4B5563);
    }
    
    .stButton button[kind="secondary"]:hover {
        background: linear-gradient(90deg, #4B5563, #374151);
    }
    
    /* Hook line - minimal spacing */
    .hook-line {
        text-align: center;
        font-size: 1.4rem;
        color: #1E40AF;
        font-weight: 700;
        margin: 0.5rem 0 1rem 0 !important;
        padding: 1rem !important;
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border-radius: 12px;
        border: 2px dashed #3B82F6;
        line-height: 1.4;
    }
    
    /* Footer - minimal spacing */
    .footer {
        text-align: center;
        padding: 1rem !important;
        margin-top: 0.5rem !important;
        color: #6B7280;
        font-size: 0.85rem;
        border-top: 1px solid #E5E7EB;
    }
    
    /* Remove spacing from ALL elements */
    p {
        margin-bottom: 0.3rem !important;
    }
    
    /* Section headers - minimal spacing */
    h2 {
        margin-top: 0.8rem !important;
        margin-bottom: 0.5rem !important;
        padding-bottom: 0.3rem;
        border-bottom: 2px solid #E5E7EB;
        color: #1F2937;
        line-height: 1.2;
    }
    
    h3 {
        margin-top: 0.5rem !important;
        margin-bottom: 0.3rem !important;
    }
    
    /* Remove spacing from expander */
    .streamlit-expanderHeader {
        margin: 0 !important;
        padding: 0.8rem !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        .card {
            padding: 1rem !important;
            margin-bottom: 0.5rem !important;
        }
        .white-box-container {
            padding: 1.8rem !important;
            margin: 0.5rem 0 0.8rem 0 !important;
        }
        .section-title {
            font-size: 1.3rem;
        }
        .sidebar-header h2 {
            font-size: 1.5rem !important;
        }
        .page-header {
            font-size: 1.8rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"
if 'visited_pages' not in st.session_state:
    st.session_state.visited_pages = set(["home"])
if 'page_scrolled' not in st.session_state:
    st.session_state.page_scrolled = False

def change_page(page_name):
    st.session_state.current_page = page_name
    st.session_state.visited_pages.add(page_name)
    st.session_state.page_scrolled = False  # Reset scroll state
    st.rerun()

def load_module(module_name, function_name):
    """Safely load and execute a module function"""
    try:
        module_path = f"modules/{module_name}.py"
        if os.path.exists(module_path):
            spec = importlib.util.spec_from_file_location(f"{module_name}_module", module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[f"{module_name}_module"] = module
            spec.loader.exec_module(module)
            
            if hasattr(module, function_name):
                getattr(module, function_name)()
                return True
            else:
                st.error(f"❌ Module {module_name} doesn't have function {function_name}")
                return False
        else:
            st.error(f"❌ Module file not found: {module_path}")
            return False
    except Exception as e:
        st.error(f"❌ Error loading {module_name}: {str(e)}")
        return False

# ================= SIDEBAR NAVIGATION - UPDATED FOR BETTER ALIGNMENT =================
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    # Header - FIXED: Centered and upward
    st.markdown('<div class="sidebar-header">', unsafe_allow_html=True)
    st.markdown("<h2>🚁 Skylark Brief</h2>", unsafe_allow_html=True)
    st.markdown("<p>AI-Powered Drone Intelligence</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Navigation
    st.markdown("### Navigation")
    
    pages = [
        ("🏠 Dashboard Home", "home"),
        ("🏢 Company Research", "research"),
        ("🔍 Market Analysis", "market"),
        ("⚙️ DMO Deep Dive", "dmo"),
        ("🚀 Confidence Engine", "confidence"),
    ]
    
    for display_name, page_id in pages:
        is_current = st.session_state.current_page == page_id
        if st.button(
            display_name,
            use_container_width=True,
            type="primary" if is_current else "secondary",
            key=f"nav_{page_id}"
        ):
            if not is_current:
                change_page(page_id)
    
    # Progress Section
    st.markdown('<div class="progress-section">', unsafe_allow_html=True)
    st.markdown("### Progress")
    
    page_files = {
        "research": "modules/research.py",
        "market": "modules/market.py",
        "dmo": "modules/dmo.py",
        "confidence": "modules/trust_engine.py",
    }
    
    completed_pages = sum(os.path.exists(path) for path in page_files.values())
    total_pages = len(page_files)
    
    progress_value = int((completed_pages / total_pages) * 100) if total_pages > 0 else 0
    st.progress(progress_value)
    
    if progress_value == 100:
        st.success("✅ All modules ready")
    else:
        st.info(f"📊 {completed_pages}/{total_pages} modules")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Creator Info
    st.markdown("---")
    st.markdown("**👤 Creator:** Pranav Rasane")
    st.markdown("**🎯 Role:** AI Engineering Candidate")
    st.markdown("**📧 Email:** pranav.rasane@gmail.com")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ================= JavaScript to force scroll to top on page change =================
if not st.session_state.page_scrolled:
    st.markdown(
        """
        <script>
            // Scroll to top when page changes
            window.scrollTo(0, 0);
            
            // Also add an anchor at the top
            window.location.hash = "";
            
            // Prevent automatic scroll restoration
            if ('scrollRestoration' in history) {
                history.scrollRestoration = 'manual';
            }
        </script>
        """,
        unsafe_allow_html=True
    )
    st.session_state.page_scrolled = True

# ================= MAIN CONTENT =================
if st.session_state.current_page == "home":
    # Main Header
    st.markdown('<h1 class="main-header">🚁 Skylark Brief: AI-Powered Drone Intelligence</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transforming Aerial Data into Confident Business Decisions</p>', unsafe_allow_html=True)
    
    # Hook Line - EXACTLY as requested
    st.markdown("""
    <div class="hook-line">
    The goal is simple but ambitious - "Turn drone operations from data-generating workflows into decision-ready systems that enterprises can trust.
    </div>
    """, unsafe_allow_html=True)
    
    # ====== FIXED: White Box with Clean HTML ======
    white_box_html = '''
    <div class="white-box-container">
        <div class="hero-title-box">🎯 Your Mission, My Analysis</div>
        <p class="hero-text-box">Imagine drone operations where every flight delivers <span class="hero-highlight">confidence, not questions</span>. Where insights move teams to action in <span class="hero-highlight">hours, not weeks</span>. Where enterprises don't second-guess data, they <span class="hero-highlight">trust it</span>.</p>
        <p class="hero-text-box">This assignment is not a surface-level analysis. It's a <span class="hero-highlight">product-first, AI-driven blueprint</span> for scaling Drone Mission Ops into a true decision platform. I've deeply studied Skylark's ecosystem, benchmarked <span class="hero-highlight">global and India-specific competitors</span>, and identified where intelligence, not just automation, delivers real competitive leverage.</p>
        <p class="hero-text-box">From <span class="hero-highlight">intelligent mission planning</span> and <span class="hero-highlight">context-aware anomaly detection</span> to <span class="hero-highlight">automated reporting</span> and a dedicated <span class="hero-highlight">Trust Layer (Confidence Engine)</span>, every insight is designed to close the gap between data capture and business conviction, helping DMO evolve from an operations tool into an <span class="hero-highlight">intelligent decision partner</span>.</p>
    </div>
    '''
    st.markdown(white_box_html, unsafe_allow_html=True)
    
    # ====== FIXED: Navigation Section with Better Alignment ======
    st.markdown('<div class="section-title-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔍 Explore the Analysis</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Dive into comprehensive insights across four strategic areas:</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Card 1
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🏢 Company Research")
        st.markdown("Unpack Skylark's three-pillar strategy: Watchtower for compliance, DMO for execution, Spectra for intelligence.")
        if st.button("Explore Research", key="home_research_btn", use_container_width=True):
            change_page("research")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Card 2
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ⚙️ DMO Deep Dive")
        st.markdown("Analyze Drone Mission Ops' data quality firewall and uncover AI opportunities for enterprise-scale operations.")
        if st.button("Analyze DMO", key="home_dmo_btn", use_container_width=True):
            change_page("dmo")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Card 3
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🔍 Market Analysis")
        st.markdown("India-first competitor benchmarking with AI clustering and strategic positioning insights.")
        if st.button("View Analysis", key="home_market_btn", use_container_width=True):
            change_page("market")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Card 4 (Featured)
        st.markdown('<div class="card card-featured">', unsafe_allow_html=True)
        st.markdown("### ⭐ Confidence Engine")
        st.markdown("**Interactive AI prototype** that transforms doubt into decisions. Experience trust scoring in action.")
        if st.button("Try Prototype Now", key="home_confidence_btn", use_container_width=True, type="primary"):
            change_page("confidence")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick Guide (simplified)
    with st.expander("💡 How to Navigate This Analysis", expanded=False):
        st.markdown("""
        **Recommended Flow:**
        1. **Start with Company Research** to understand Skylark's foundation
        2. **Explore Market Analysis** to see the competitive landscape
        3. **Dive into DMO** to understand current capabilities
        4. **Experience the Confidence Engine** (the core AI innovation)
        """)

# COMPANY RESEARCH PAGE
elif st.session_state.current_page == "research":
    # Force scroll to top for this page
    if not st.session_state.page_scrolled:
        st.markdown(
            """
            <script>
                window.scrollTo(0, 0);
            </script>
            """,
            unsafe_allow_html=True
        )
        st.session_state.page_scrolled = True
    
    if not load_module("research", "show_research_page"):
        st.markdown('<h1 class="page-header">🏢 Company Research</h1>', unsafe_allow_html=True)
        st.info("Research module loading...")

# MARKET ANALYSIS PAGE
elif st.session_state.current_page == "market":
    # Force scroll to top for this page
    if not st.session_state.page_scrolled:
        st.markdown(
            """
            <script>
                window.scrollTo(0, 0);
            </script>
            """,
            unsafe_allow_html=True
        )
        st.session_state.page_scrolled = True
    
    if not load_module("market", "show_market_page"):
        st.markdown('<h1 class="page-header">🔍 Market Analysis</h1>', unsafe_allow_html=True)
        st.info("Market analysis module loading...")

# DMO DEEP DIVE PAGE
elif st.session_state.current_page == "dmo":
    # Force scroll to top for this page
    if not st.session_state.page_scrolled:
        st.markdown(
            """
            <script>
                window.scrollTo(0, 0);
            </script>
            """,
            unsafe_allow_html=True
        )
        st.session_state.page_scrolled = True
    
    if not load_module("dmo", "show_dmo_page"):
        st.markdown('<h1 class="page-header">⚙️ DMO Deep Dive</h1>', unsafe_allow_html=True)
        st.info("DMO analysis module loading...")

# CONFIDENCE ENGINE PAGE
elif st.session_state.current_page == "confidence":
    # Force scroll to top for this page
    if not st.session_state.page_scrolled:
        st.markdown(
            """
            <script>
                window.scrollTo(0, 0);
            </script>
            """,
            unsafe_allow_html=True
        )
        st.session_state.page_scrolled = True
    
    module_name = "trust_engine" if os.path.exists("modules/trust_engine.py") else "confidence"
    function_name = "show_trust_engine_page" if os.path.exists("modules/trust_engine.py") else "show_confidence_page"
    
    if not load_module(module_name, function_name):
        st.markdown('<h1 class="page-header">🚀 Confidence Engine</h1>', unsafe_allow_html=True)
        st.info("Confidence Engine module loading...")

# ================= FOOTER =================

# Research disclaimer
st.caption(
    "🔍 **Research Integrity:** All insights derived from publicly available Skylark Drones documentation. "
    "No confidential information or internal assumptions."
)

# Footer
st.markdown("""
<div class="footer">
© 2026 Pranav Rasane • AI Engineering Role Assignment • Skylark Drones Analysis<br>
<small>Demonstrating strategic AI thinking for enterprise drone intelligence</small>
</div>
""", unsafe_allow_html=True)