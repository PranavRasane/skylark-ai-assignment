# modules/trust_engine.py - CONTEXTUAL CONFIDENCE ENGINE (FLAGSHIP AI PROTOTYPE)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

def show_trust_engine_page():
    st.title("🚀 Contextual Confidence Engine")
    st.markdown("---")
    
    # ================= INTRODUCTION =================
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        ### 🎯 **The Problem: Drone Data Doubt**
        
        Drone surveys capture incredible precision, yet decision-makers hesitate.
        The gap between **data collection** and **data conviction** is the industry's 
        biggest bottleneck.
        
        **This prototype demonstrates how AI can bridge that gap.**
        """)
    with col2:
        st.metric("Trust Impact", "High", delta="Decision Speed 3x", delta_color="off")
        st.metric("False Positives", "Reduced", delta="-70%", delta_color="inverse")
    
    st.warning("""
    ⚠️ **Disclaimer:** This is a conceptual AI prototype demonstrating confidence scoring logic. 
    It simulates how a Trust Layer could work with DMO and Spectra, not a production system.
    """)
    
    # ================= THE PROBLEM VISUALIZATION =================
    st.subheader("🔍 The Trust Gap: Why Decisions Get Stuck")
    
    with st.expander("📉 Visualizing the Problem", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem; background: #FEE2E2; border-radius: 10px;">
            <h3 style="color: #991B1B;">📊 Inconsistent Results</h3>
            <p style="color: #991B1B;">
            Same site, different measurements. Is this real change or noise?
            </p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem; background: #FEF3C7; border-radius: 10px;">
            <h3 style="color: #92400E;">🤖 AI Without Context</h3>
            <p style="color: #92400E;">
            Alerts with no confidence levels. Every flag feels equally urgent.
            </p>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem; background: #DBEAFE; border-radius: 10px;">
            <h3 style="color: #1E40AF;">📝 No Clear Priorities</h3>
            <p style="color: #1E40AF;">
            Hundreds of observations. Which ones need immediate action?
            </p>
            </div>
            """, unsafe_allow_html=True)
    
    # ================= HOW THE CONFIDENCE ENGINE WORKS =================
    st.subheader("⚙️ How the Confidence Engine Works")
    
    st.markdown("""
    **Four-Step Process to Transform Raw Data into Confident Decisions:**
    """)
    
    steps = [
        {
            "step": "1️⃣",
            "title": "Cross-Examination Detective",
            "description": "Analyzes data against historical, environmental, and sensor context",
            "icon": "🔍",
            "color": "#3B82F6"
        },
        {
            "step": "2️⃣",
            "title": "Confidence Scoring",
            "description": "Assigns confidence scores (0-100%) with clear explanations",
            "icon": "📊",
            "color": "#10B981"
        },
        {
            "step": "3️⃣",
            "title": "Traffic Light Action System",
            "description": "Prioritizes findings: Green (Act Now), Yellow (Review), Red (Monitor)",
            "icon": "🚦",
            "color": "#F59E0B"
        },
        {
            "step": "4️⃣",
            "title": "Continuous Learning",
            "description": "Improves accuracy based on human feedback and corrections",
            "icon": "🧠",
            "color": "#8B5CF6"
        }
    ]
    
    # Display steps in a grid
    cols = st.columns(4)
    for idx, step in enumerate(steps):
        with cols[idx]:
            st.markdown(f"""
            <div style="
                text-align: center;
                padding: 1.5rem;
                background: linear-gradient(135deg, {step['color']}15 0%, {step['color']}08 100%);
                border-radius: 10px;
                border-top: 4px solid {step['color']};
                height: 100%;
                margin-bottom: 1rem;
            ">
                <h1 style="margin: 0; font-size: 2.5rem;">{step['icon']}</h1>
                <h3 style="margin: 0.5rem 0; color: {step['color']};">{step['step']}</h3>
                <p style="margin: 0.5rem 0; font-weight: bold; color: #1F2937;">{step['title']}</p>
                <p style="margin: 0; color: #6B7280; font-size: 0.9rem;">{step['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # ================= INTERACTIVE PROTOTYPE =================
    st.subheader("🎮 Interactive Confidence Engine Prototype")
    
    st.info("""
    👆 **Try it:** Adjust the mission parameters below to see how the Confidence Engine 
    evaluates data quality and provides actionable insights.
    """)
    
    # Mission Parameters Sliders
    st.markdown("### 📋 Mission Parameters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        image_quality = st.slider(
            "📸 Image Quality", 
            min_value=0, max_value=100, value=85,
            help="Overall clarity and sharpness of captured images"
        )
        lighting_conditions = st.select_slider(
            "🌤️ Lighting Conditions", 
            options=["Poor", "Fair", "Good", "Excellent"],
            value="Good"
        )
        
    with col2:
        overlap_consistency = st.slider(
            "📐 Overlap Consistency", 
            min_value=0, max_value=100, value=90,
            help="Consistency of image overlap across the mission"
        )
        wind_speed = st.slider(
            "💨 Wind Speed (km/h)", 
            min_value=0, max_value=50, value=15,
            help="Wind conditions during flight"
        )
        
    with col3:
        historical_match = st.slider(
            "📊 Historical Pattern Match", 
            min_value=0, max_value=100, value=75,
            help="Similarity to past successful missions"
        )
        sensor_calibration = st.select_slider(
            "⚙️ Sensor Calibration", 
            options=["Expired", "Marginal", "Good", "Excellent"],
            value="Good"
        )
    
    # Asset Type Selection
    st.markdown("### 🏭 Asset Configuration")
    
    asset_col1, asset_col2 = st.columns(2)
    
    with asset_col1:
        asset_type = st.selectbox(
            "Select Asset Type",
            ["Mining Stockpile", "Solar Farm", "Road Infrastructure", "Building Inspection", "Agricultural Field"],
            index=0
        )
        
        # Asset-specific parameters
        if asset_type == "Mining Stockpile":
            asset_importance = "High"
            measurement_impact = "Volume calculation accuracy critical"
            historical_data_points = "45+ past surveys"
        elif asset_type == "Solar Farm":
            asset_importance = "Critical"
            measurement_impact = "Fault detection affects energy output"
            historical_data_points = "120+ past inspections"
        elif asset_type == "Road Infrastructure":
            asset_importance = "Medium"
            measurement_impact = "Safety compliance monitoring"
            historical_data_points = "30+ past surveys"
        else:
            asset_importance = "Medium"
            measurement_impact = "General inspection"
            historical_data_points = "20+ past surveys"
    
    with asset_col2:
        mission_criticality = st.selectbox(
            "Mission Criticality",
            ["Routine Inspection", "Progress Monitoring", "Compliance Check", "Emergency Assessment"],
            index=1
        )
        
        st.markdown(f"""
        **Asset Details:**
        - **Importance:** {asset_importance}
        - **Measurement Impact:** {measurement_impact}
        - **Historical Data:** {historical_data_points}
        """)
    
    # ================= CONFIDENCE CALCULATION =================
    st.markdown("### ⚡ Confidence Engine Analysis")
    
    # Calculate confidence score based on inputs
    def calculate_confidence_score():
        # Base weights
        weights = {
            "image_quality": 0.25,
            "lighting": 0.20,
            "overlap": 0.20,
            "wind": 0.15,
            "historical": 0.10,
            "sensor": 0.10
        }
        
        # Convert categorical values to numeric
        lighting_score = {
            "Poor": 40, "Fair": 65, "Good": 85, "Excellent": 95
        }[lighting_conditions]
        
        sensor_score = {
            "Expired": 30, "Marginal": 60, "Good": 85, "Excellent": 95
        }[sensor_calibration]
        
        # Wind penalty (higher wind = lower score)
        wind_penalty = max(0, 100 - (wind_speed * 2))
        
        # Calculate weighted score
        score = (
            image_quality * weights["image_quality"] +
            lighting_score * weights["lighting"] +
            overlap_consistency * weights["overlap"] +
            wind_penalty * weights["wind"] +
            historical_match * weights["historical"] +
            sensor_score * weights["sensor"]
        )
        
        # Asset type adjustment
        asset_adjustment = {
            "Mining Stockpile": 0,  # No adjustment
            "Solar Farm": 5,        # Slightly more critical
            "Road Infrastructure": -2,
            "Building Inspection": 0,
            "Agricultural Field": -3
        }[asset_type]
        
        return min(100, max(0, score + asset_adjustment))
    
    # Generate insights
    def generate_insights(confidence_score):
        insights = []
        
        # Main insight
        if confidence_score >= 90:
            insights.append({
                "level": "green",
                "message": f"✅ **Excellent Data Quality** ({confidence_score:.1f}%)",
                "details": "Data is highly reliable for decision-making. Automated actions recommended."
            })
        elif confidence_score >= 75:
            insights.append({
                "level": "yellow",
                "message": f"⚠️ **Good Data with Minor Concerns** ({confidence_score:.1f}%)",
                "details": "Data is reliable for most decisions. Review recommended for critical measurements."
            })
        else:
            insights.append({
                "level": "red",
                "message": f"❌ **Data Quality Concerns** ({confidence_score:.1f}%)",
                "details": "Significant uncertainties detected. Manual verification recommended before action."
            })
        
        # Specific insights based on parameters
        if image_quality < 70:
            insights.append({
                "level": "red",
                "message": "📸 **Image Quality Issue**",
                "details": f"Image quality ({image_quality}%) may affect measurement accuracy."
            })
        elif image_quality > 90:
            insights.append({
                "level": "green",
                "message": "📸 **Excellent Image Quality**",
                "details": "Clear, sharp imagery supports high-confidence analysis."
            })
            
        if wind_speed > 25:
            insights.append({
                "level": "red",
                "message": "💨 **High Wind Impact**",
                "details": f"Wind speed ({wind_speed} km/h) may cause image blur and position errors."
            })
            
        if historical_match < 60:
            insights.append({
                "level": "yellow",
                "message": "📊 **Historical Pattern Deviation**",
                "details": "Significant deviation from historical patterns. May indicate real change or anomaly."
            })
            
        if sensor_calibration == "Expired":
            insights.append({
                "level": "red",
                "message": "⚙️ **Sensor Calibration Expired**",
                "details": "Sensor calibration is expired. Measurements may have systematic errors."
            })
        
        return insights
    
    # Calculate and display confidence
    confidence_score = calculate_confidence_score()
    insights = generate_insights(confidence_score)
    
    # Display confidence with gauge chart
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create gauge chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = confidence_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Overall Confidence Score", 'font': {'size': 20}},
            delta = {'reference': 80, 'increasing': {'color': "green"}, 'decreasing': {'color': "red"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': 'red'},
                    {'range': [50, 75], 'color': 'yellow'},
                    {'range': [75, 100], 'color': 'green'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        fig.update_layout(
            height=300,
            margin=dict(l=10, r=10, t=50, b=10)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Display score interpretation
        st.markdown(f"""
        <div style="
            padding: 1.5rem;
            border-radius: 10px;
            background: {'#DCFCE7' if confidence_score >= 75 else '#FEF3C7' if confidence_score >= 50 else '#FEE2E2'};
            border-left: 5px solid {'#16A34A' if confidence_score >= 75 else '#F59E0B' if confidence_score >= 50 else '#DC2626'};
            height: 100%;
        ">
            <h3 style="margin-top: 0; color: {'#166534' if confidence_score >= 75 else '#92400E' if confidence_score >= 50 else '#991B1B'};">Score Interpretation</h3>
            <p style="margin-bottom: 0.5rem; color: #1F2937;">
            <strong>{confidence_score:.1f}%</strong> confidence in data reliability
            </p>
            <p style="color: #4B5563; font-size: 0.9rem;">
            {'High reliability for business decisions' if confidence_score >= 75 else 'Moderate reliability, review recommended' if confidence_score >= 50 else 'Significant concerns, verification needed'}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # ================= INSIGHTS & RECOMMENDATIONS =================
    st.markdown("### 🔍 Detailed Insights & Recommendations")
    
    # Display insights
    for insight in insights:
        if insight["level"] == "green":
            st.success(f"**{insight['message']}**\n\n{insight['details']}")
        elif insight["level"] == "yellow":
            st.warning(f"**{insight['message']}**\n\n{insight['details']}")
        else:
            st.error(f"**{insight['message']}**\n\n{insight['details']}")
    
    # ================= ACTION PRIORITIZATION =================
    st.subheader("🚦 Action Prioritization (Traffic Light System)")
    
    # Generate sample findings based on asset type
    def generate_sample_findings(asset_type, confidence_score):
        if asset_type == "Mining Stockpile":
            return [
                {"id": "VOL-001", "type": "Volume Measurement", "value": "52,430 m³", "confidence": confidence_score},
                {"id": "SLP-001", "type": "Slope Stability", "value": "32°", "confidence": max(0, confidence_score - 15)},
                {"id": "ERD-001", "type": "Erosion Detection", "value": "Minor", "confidence": max(0, confidence_score - 25)},
                {"id": "EQP-001", "type": "Equipment Presence", "value": "Detected", "confidence": min(100, confidence_score + 10)},
            ]
        elif asset_type == "Solar Farm":
            return [
                {"id": "THM-001", "type": "Thermal Anomaly", "value": "Panel A7", "confidence": max(0, confidence_score - 10)},
                {"id": "DTR-001", "type": "Dirt Accumulation", "value": "Low", "confidence": confidence_score},
                {"id": "STR-001", "type": "Structural Integrity", "value": "Normal", "confidence": min(100, confidence_score + 5)},
                {"id": "CON-001", "type": "Connection Check", "value": "All OK", "confidence": min(100, confidence_score + 15)},
            ]
        else:
            return [
                {"id": "CRK-001", "type": "Crack Detection", "value": "Minor", "confidence": confidence_score},
                {"id": "WAR-001", "type": "Wear Analysis", "value": "Normal", "confidence": min(100, confidence_score + 5)},
                {"id": "ALG-001", "type": "Alignment Check", "value": "Within Spec", "confidence": max(0, confidence_score - 5)},
                {"id": "CLN-001", "type": "Cleanliness", "value": "Good", "confidence": min(100, confidence_score + 10)},
            ]
    
    findings = generate_sample_findings(asset_type, confidence_score)
    
    # Display findings in prioritized order
    st.markdown("#### 📋 Prioritized Findings")
    
    for finding in findings:
        col1, col2, col3, col4 = st.columns([1, 2, 1, 2])
        
        with col1:
            # Color code based on confidence
            if finding["confidence"] >= 85:
                color = "🟢"
                action = "ACT NOW"
            elif finding["confidence"] >= 70:
                color = "🟡"
                action = "REVIEW"
            else:
                color = "🔴"
                action = "MONITOR"
            st.markdown(f"### {color}")
            
        with col2:
            st.markdown(f"**{finding['type']}**")
            st.markdown(f"*{finding['id']}*")
            
        with col3:
            st.markdown(f"**{finding['value']}**")
            
        with col4:
            confidence_color = (
                "green" if finding["confidence"] >= 85 else 
                "orange" if finding["confidence"] >= 70 else 
                "red"
            )
            st.markdown(f"""
            <div style="
                display: inline-block;
                padding: 0.25rem 0.75rem;
                background-color: {confidence_color}20;
                color: {confidence_color};
                border-radius: 20px;
                font-weight: bold;
                border: 1px solid {confidence_color}40;
            ">
            {finding['confidence']:.0f}% • {action}
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
    
    # ================= BUSINESS IMPACT CALCULATOR =================
    st.subheader("💰 Business Impact Analysis")
    
    with st.expander("📈 ROI Calculator for Confidence Engine", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            monthly_surveys = st.number_input("Monthly Surveys", min_value=1, max_value=100, value=12)
            avg_survey_cost = st.number_input("Average Survey Cost (₹)", min_value=10000, max_value=1000000, value=250000, step=10000)
            
        with col2:
            re_flight_rate = st.slider("Current Re-flight Rate (%)", min_value=0, max_value=50, value=25) / 100
            decision_delay_days = st.slider("Current Decision Delay (days)", min_value=0, max_value=30, value=7)
            
        with col3:
            confidence_improvement = st.slider("Confidence Engine Improvement (%)", min_value=10, max_value=90, value=60) / 100
            
        # Calculate impact
        current_reflights = monthly_surveys * re_flight_rate
        improved_reflights = current_reflights * (1 - confidence_improvement)
        reflight_savings = (current_reflights - improved_reflights) * avg_survey_cost
        
        current_decision_days = monthly_surveys * decision_delay_days
        improved_decision_days = current_decision_days * (1 - confidence_improvement * 0.7)  # Assuming 70% of delay is due to uncertainty
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "Annual Re-flight Savings", 
                f"₹{reflight_savings * 12:,.0f}",
                delta=f"{(1 - confidence_improvement) * 100:.0f}% reduction"
            )
        with col2:
            st.metric(
                "Decision Speed Improvement", 
                f"{current_decision_days - improved_decision_days:.0f} days/month",
                delta=f"{(1 - (improved_decision_days / current_decision_days)) * 100:.0f}% faster"
            )
        with col3:
            st.metric(
                "Trust Factor", 
                "High",
                delta="Reduced manual verification"
            )
    
    # ================= INTEGRATION WITH DMO & SPECTRA =================
    st.subheader("🔄 Integration with Skylark Ecosystem")
    
    st.markdown("""
    **How Confidence Engine Enhances Existing Products:**
    
    | Product | Current Role | With Confidence Engine |
    |---------|-------------|------------------------|
    | **📡 Watchtower** | Airspace safety & compliance | **Confidence-aware mission timing** (recommends optimal windows) |
    | **⚙️ DMO** | Mission planning & data QC | **Confidence-scored QC results** (not just pass/fail) |
    | **📊 Spectra** | Analytics & insights | **Confidence-weighted reporting** (prioritized insights) |
    
    **Integration Benefits:**
    - **Seamless workflow:** Confidence scores flow from DMO to Spectra
    - **Explainable AI:** Clear reasons for confidence levels
    - **Actionable output:** Traffic-light system for easy decision-making
    - **Continuous learning:** Improves with every mission and user feedback
    """)
    
    # ================= ARCHITECTURE OVERVIEW =================
    with st.expander("🏗️ Technical Architecture Overview", expanded=False):
        st.markdown("""
        ### System Components
        
        **1. Data Fusion Layer**
        - Combines mission data with historical patterns
        - Integrates environmental context (weather, lighting)
        - Validates sensor calibration status
        
        **2. Confidence Scoring Engine**
        - Machine learning models for different asset types
        - Rule-based logic for edge cases
        - Explainability module (shows "why")
        
        **3. Action Prioritization Module**
        - Traffic-light system for findings
        - Business rule integration
        - Customizable thresholds per client
        
        **4. Learning Loop**
        - Collects user feedback on confidence scores
        - Continuously improves scoring accuracy
        - Adapts to specific site conditions
        """)
        
        # Simple architecture diagram
        st.markdown("""
        ### Data Flow
        
        ```
        [DMO Mission Data] 
            ↓
        [Contextual Confidence Engine]
            ├── Historical Pattern Analysis
            ├── Environmental Context
            ├── Sensor Data Validation
            └── Asset-Specific Rules
            ↓
        [Confidence Scores + Insights]
            ↓
        [DMO QC Results] → [Spectra Analytics]
            ↓
        [Business Decisions with Confidence Levels]
        ```
        """)
    
    # ================= VALIDATION & NEXT STEPS =================
    st.markdown("---")
    
    st.success("""
    ✅ **Confidence Engine Prototype Complete**
    
    **Key Capabilities Demonstrated:**
    
    1. **Context-aware confidence scoring** based on multiple factors
    2. **Action prioritization** with traffic-light system
    3. **Business impact analysis** showing clear ROI
    4. **Seamless integration** with existing DMO + Spectra workflow
    
    **Next Steps for Implementation:**
    
    1. **Phase 1:** Integrate basic confidence scoring into DMO QC results
    2. **Phase 2:** Add historical pattern analysis for specific asset types
    3. **Phase 3:** Develop learning loop based on user feedback
    4. **Phase 4:** Expand to predictive confidence for future missions
    
    **The Bottom Line:** This transforms drone data from "maybe accurate" to "confidently actionable."
    """)

# If running this module directly for testing
if __name__ == "__main__":
    if "current_page" not in st.session_state:
        st.session_state.current_page = "confidence"
    show_trust_engine_page()