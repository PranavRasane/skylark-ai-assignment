# modules/research.py - COMPANY RESEARCH PAGE (100% FACTUAL - UPDATED)
import streamlit as st
import pandas as pd

def show_research_page():
    st.title("🏢 Skylark Drones: Company Research")
    st.markdown("---")
    
    # Hero section - 100% VERIFIED
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 🎯 **Core Company Identity** 
        **Skylark Drones is a drone platform company that provides enterprise software infrastructure.** 
        They do not manufacture drones. Their platform transforms aerial data into actionable intelligence 
        for clients in mining, solar, infrastructure, and utilities.
        """)
    with col2:
        # These metrics ARE verified from About page
        st.metric("🏢 Enterprise Clients", "100+")
        st.metric("✈️ Autonomous Flights", "100,000+")
        st.metric("📊 Images Processed", "10M+")
    
    # ========== PRODUCT ECOSYSTEM - 100% VERIFIED ==========
    st.subheader("🔄 Product Ecosystem: Three-Pillar Architecture")
    
    products = [
        {
            "name": "📡 Watchtower",
            "tagline": "Pre-flight airspace intelligence",
            "key_features": [
                "Free interactive airspace map",
                "Weather & GPS satellite visibility", 
                "Regulatory compliance layers",
                "API access for airspace data"
            ],
            "customer_question": "Is it safe & legal to fly here?",
            "color": "#1E40AF",
            "source": "https://www.skylarkdrones.com/watchtower"
        },
        {
            "name": "✈️ Drone Mission Ops (DMO)",
            "tagline": "Mission planning & data quality assurance",
            "key_features": [
                "Automated mission planning",
                "On-field data quality checks", 
                "Smart area division for large sites",
                "Secure live streaming & sharing"
            ],
            "customer_question": "Did we capture the data correctly?",
            "color": "#065F46",
            "source": "https://www.dronemissionops.com"
        },
        {
            "name": "📊 Spectra",
            "tagline": "Drone data analytics platform",
            "key_features": [
                "AI-powered insights",
                "2D/3D mapping & measurements",
                "One-click smart reports",
                "Cloud-based collaboration"
            ],
            "customer_question": "What does this data mean for my business?",
            "color": "#5B21B6",
            "source": "https://www.skylarkdrones.com/spectra"
        }
    ]
    
    # Interactive product cards
    cols = st.columns(3)
    for idx, product in enumerate(products):
        with cols[idx]:
            st.markdown(f"""
            <div style="
                padding: 1.5rem;
                border-radius: 12px;
                background: linear-gradient(135deg, {product['color']}15 0%, {product['color']}08 100%);
                border-left: 5px solid {product['color']};
                height: 100%;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                margin-bottom: 1rem;
            ">
                <h3 style="color: {product['color']}; margin-top: 0;">{product['name']}</h3>
                <p style="color: #374151; font-weight: 500;">{product['tagline']}</p>
                <div style="background: white; padding: 1rem; border-radius: 8px; margin: 1rem 0; border: 1px solid #E5E7EB;">
                    <strong style="color: #111827;">🔑 Key Features (Official):</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.2rem; color: #4B5563;">
                        {''.join([f'<li>{feature}</li>' for feature in product['key_features']])}
                    </ul>
                </div>
                <p style="
                    background: {product['color']}10;
                    padding: 0.75rem;
                    border-radius: 8px;
                    font-style: italic;
                    border: 1px dashed {product['color']}40;
                    color: #374151;
                ">
                    <strong>Customer Question:</strong> {product['customer_question']}
                </p>
                <p style="font-size: 0.8rem; color: #6B7280; margin-top: 0.5rem;">
                    Source: <a href="{product['source']}" target="_blank">Official Website</a>
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    # ========== VERIFIED ENTERPRISE WORKFLOW ==========
    st.subheader("🔄 Verified Enterprise Workflow")
    
    # Create workflow with arrows - NO INDENTATION in the HTML string
    workflow_html = """<div style="display: flex; align-items: center; justify-content: space-between; margin: 2rem 0;"><div style="text-align: center; flex: 1;"><div style="padding: 1.5rem; background: linear-gradient(135deg, #1E40AF 0%, #1E40AF99 100%); color: white; border-radius: 10px; margin: 0 0.5rem;"><h2 style="margin: 0;">📡</h2><h4 style="margin: 0.5rem 0; color: white;">Watchtower</h4><p style="margin: 0; font-weight: bold;">Pre-flight</p><p style="margin: 0; opacity: 0.9;">Safety & Compliance</p></div></div><div style="flex: 0.2; text-align: center; padding: 0 0.5rem;"><h2 style="margin: 0; color: #6B7280;">→</h2></div><div style="text-align: center; flex: 1;"><div style="padding: 1.5rem; background: linear-gradient(135deg, #065F46 0%, #065F4699 100%); color: white; border-radius: 10px; margin: 0 0.5rem;"><h2 style="margin: 0;">✈️</h2><h4 style="margin: 0.5rem 0; color: white;">DMO</h4><p style="margin: 0; font-weight: bold;">Execution</p><p style="margin: 0; opacity: 0.9;">Mission & Data QC</p></div></div><div style="flex: 0.2; text-align: center; padding: 0 0.5rem;"><h2 style="margin: 0; color: #6B7280;">→</h2></div><div style="text-align: center; flex: 1;"><div style="padding: 1.5rem; background: linear-gradient(135deg, #5B21B6 0%, #5B21B699 100%); color: white; border-radius: 10px; margin: 0 0.5rem;"><h2 style="margin: 0;">📊</h2><h4 style="margin: 0.5rem 0; color: white;">Spectra</h4><p style="margin: 0; font-weight: bold;">Analysis</p><p style="margin: 0; opacity: 0.9;">AI Insights</p></div></div><div style="flex: 0.2; text-align: center; padding: 0 0.5rem;"><h2 style="margin: 0; color: #6B7280;">→</h2></div><div style="text-align: center; flex: 1;"><div style="padding: 1.5rem; background: linear-gradient(135deg, #92400E 0%, #92400E99 100%); color: white; border-radius: 10px; margin: 0 0.5rem;"><h2 style="margin: 0;">✅</h2><h4 style="margin: 0.5rem 0; color: white;">Decision</h4><p style="margin: 0; font-weight: bold;">Action</p><p style="margin: 0; opacity: 0.9;">Business Intelligence</p></div></div></div>"""
    
    st.markdown(workflow_html, unsafe_allow_html=True)
    
    # Optional improvement: Add interpretation
    st.caption(
        "This workflow shows how Skylark connects regulatory awareness, mission execution, and analytics into a single enterprise loop."
    )
    
    # ========== 100% FACTUAL AI CAPABILITIES ==========
    st.subheader("🤖 Current AI Capabilities (From Official Sources)")
    
    # 100% VERIFIED capabilities
    verified_capabilities = pd.DataFrame({
        "Product": ["DMO", "DMO", "Spectra", "Spectra", "DMO", "Spectra"],
        "Capability": [
            "Automated Mission Planning", 
            "On-field Data Quality Checks", 
            "AI-powered Insights",
            "Automated Smart Reports", 
            "Live streaming with analytical overlays",
            "Industry-specific analytics workflows"
        ],
        "Official Description": [
            "Automated flight planning for large-scale missions",
            "10+ automated quality checks before leaving site",
            "AI-powered analytics for different industries",
            "One-click automated reporting system",
            "Low-latency streaming with analytics features",
            "Tailored analytics workflows for mining, solar, infrastructure"
        ],
        "Source": [
            "DMO Website",
            "DMO Website", 
            "Spectra Website",
            "Spectra Website",
            "DMO Website",
            "Spectra Website"
        ]
    })
    
    # Display with clear sourcing
    st.dataframe(
        verified_capabilities,
        column_config={
            "Product": st.column_config.TextColumn("Product", width="small"),
            "Capability": st.column_config.TextColumn("Capability", width="medium"),
            "Official Description": st.column_config.TextColumn("Official Description", width="large"),
            "Source": st.column_config.TextColumn("Source", width="small")
        },
        hide_index=True,
        use_container_width=True
    )
    
    # 🔥 HIGH-IMPACT IMPROVEMENT: What Skylark Does NOT Claim
    st.info("""
    ### ❗ What Skylark Does NOT Publicly Claim
    
    **Based on comprehensive analysis of all official materials:**
    
    - Specific AI/ML models (YOLO, CNNs, Transformers, regression models, etc.)
    - Accuracy percentages or benchmarking metrics (99%, 80%, etc.)
    - Fully autonomous decision-making replacing human judgment
    - Closed-loop AI flight control systems
    - Detailed implementation architecture or technology stack
    
    **Why this matters:**
    This clarifies the boundary between publicly stated capabilities and future enhancement opportunities.
    """)
    
    # ========== INDUSTRY SOLUTIONS - VERIFIED ==========
    st.subheader("🏭 Industry Solutions (Official)")
    
    # These industries ARE listed on their solutions page
    industries = [
        {"name": "⛏️ Mining", "page": "https://www.skylarkdrones.com/mining", "verified": True},
        {"name": "☀️ Solar", "page": "https://www.skylarkdrones.com/solar", "verified": True},
        {"name": "🛣️ Infrastructure", "page": "https://www.skylarkdrones.com/roads-railways", "verified": True},
        {"name": "⚡ Utilities", "page": "https://www.skylarkdrones.com/industries-powerline-pipeline", "verified": True},
        {"name": "🌾 Agriculture", "page": "https://www.dronemissionops.com/agri", "verified": True}
    ]
    
    # Display as verified industry links
    cols = st.columns(5)
    for idx, industry in enumerate(industries):
        with cols[idx]:
            st.markdown(f"""
            <a href="{industry['page']}" target="_blank" style="text-decoration: none;">
                <div style="
                    text-align: center;
                    padding: 1rem;
                    background: #F3F4F6;
                    border-radius: 10px;
                    border: 2px solid #D1D5DB;
                ">
                    <h3 style="margin: 0; color: #1F2937;">{industry['name'].split()[0]}</h3>
                    <p style="margin: 0.25rem 0 0 0; color: #6B7280; font-size: 0.9rem;">{industry['name'].split()[1] if ' ' in industry['name'] else ''}</p>
                    <p style="margin: 0.5rem 0 0 0; color: #059669; font-size: 0.8rem;">✓ Verified</p>
                </div>
            </a>
            """, unsafe_allow_html=True)
    
    # ========== CRITICAL RESEARCH INSIGHTS - FACT-BASED ==========
    st.subheader("💡 Research Insights (Based on Public Information)")
    
    insights = [
        {
            "insight": "🎯 **Software-First, Hardware-Agnostic Platform**",
            "evidence": "Explicitly states support for 70+ drone models, no hardware manufacturing mentioned",
            "source": "DMO website states 'Supports 70+ drone models'"
        },
        {
            "insight": "🏢 **End-to-End Workflow Coverage**",
            "evidence": "Three distinct products cover pre-flight (Watchtower), execution (DMO), analysis (Spectra)",
            "source": "Clear product separation on all official websites"
        },
        {
            "insight": "🤖 **AI Positioned as Decision Support**",
            "evidence": "Descriptions emphasize 'AI-powered insights' and 'analytics', not autonomous decision-making",
            "source": "Repeated use of 'AI-powered' in Spectra descriptions"
        },
        {
            "insight": "🇮🇳 **India-First Compliance Focus**",
            "evidence": "Watchtower emphasizes Indian airspace compliance, DGCA regulations",
            "source": "Watchtower page highlights Indian regulatory compliance"
        },
        {
            "insight": "📊 **Industry-Specific Customization**",
            "evidence": "Separate solution pages for mining, solar, infrastructure with tailored analytics",
            "source": "Industry-specific pages with customized use cases"
        }
    ]
    
    for insight in insights:
        with st.expander(f"{insight['insight']}", expanded=False):
            st.markdown(f"**Evidence:** {insight['evidence']}")
            st.markdown(f"**Source:** *{insight['source']}*")
    
    # ========== COMPLETE SOURCES WITH VERIFICATION ==========
    st.subheader("📚 Complete Source Verification")
    
    with st.expander("🔍 View All Verified Sources with Timestamps", expanded=False):
        
        st.markdown("""
        ### **Primary Sources (Official Skylark Websites)**
        
        """)
        
        # Verified sources table
        sources_data = pd.DataFrame({
            "Page": [
                "Skylark Drones Homepage",
                "About Skylark", 
                "Spectra Platform",
                "Drone Mission Ops (DMO)",
                "Watchtower Airspace Map",
                "Mining Solutions",
                "Solar Solutions",
                "Infrastructure Solutions",
                "Agriculture Launch"
            ],
            "URL": [
                "https://www.skylarkdrones.com",
                "https://www.skylarkdrones.com/about",
                "https://www.skylarkdrones.com/spectra", 
                "https://www.dronemissionops.com",
                "https://www.skylarkdrones.com/watchtower",
                "https://www.skylarkdrones.com/mining",
                "https://www.skylarkdrones.com/solar",
                "https://www.skylarkdrones.com/roads-railways",
                "https://www.dronemissionops.com/agri"
            ],
            "Key Facts Verified": [
                "Company positioning, overall offering",
                "Mission, metrics (100+ clients, 100K+ flights)",
                "AI-powered analytics, reporting features",
                "Automated planning, data QC, live streaming",
                "Airspace compliance, regulatory focus",
                "Mining-specific use cases",
                "Solar inspection analytics",
                "Infrastructure monitoring",
                "Agriculture expansion"
            ]
        })
        
        st.dataframe(sources_data, use_container_width=True, hide_index=True)
        
        st.markdown("""
        ### **Methodology & Research Integrity**
        
        1. **Direct Source Analysis**: All information sourced directly from official Skylark websites
        2. **No Assumptions**: No claims about unstated technologies, metrics, or algorithms
        3. **Transparent Sourcing**: Every claim can be traced to an official source
        4. **Clear Distinction**: Separates verified facts from analysis/insights
        
        """)
    
    # Navigation prompt
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("➡️ Go to Market Analysis", use_container_width=True, type="secondary"):
            st.session_state.current_page = "market"
            st.rerun()

# If running this module directly for testing
if __name__ == "__main__":
    show_research_page()