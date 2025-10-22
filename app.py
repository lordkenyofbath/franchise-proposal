import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Lebanese Fast-Casual Franchise | Strategic Proposal",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #ff6b35 0%, #dc2f02 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #ff6b35;
        margin: 1rem 0;
    }
    .phase-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #28a745;
    }
    .value-highlight {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .price-card {
        background: linear-gradient(135deg, #ff6b35 0%, #dc2f02 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📋 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Executive Summary", "Deliverables", "Value Proposition", "Investment", "Timeline"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Project Scope:**  
Complete franchise development from market research through operational blueprint and franchise system architecture.

**Total Work:** ~200 hours  
**Documentation:** 120+ pages
""")

if page == "Executive Summary":
    st.markdown("""
    <div class="main-header">
        <h1>🍽️ Lebanese Fast-Casual Franchise</h1>
        <h3>Strategic Franchise Development | Singapore Market</h3>
        <p style="margin-top: 1rem; opacity: 0.9;">Complete Business Plan & Franchise-Ready System</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Development Phases", "4", delta="Complete")
    with col2:
        st.metric("Store Capacity (SG)", "25-30", delta="Analyzed")
    with col3:
        st.metric("ROI Timeline", "3-5 years", delta="Per Store")
    with col4:
        st.metric("Documentation", "120+ pages", delta="Delivered")
    
    st.markdown("---")
    
    st.header("📊 Project Overview")
    
    st.markdown("""
    <div class="metric-card">
        <h3>🎯 Strategic Objective</h3>
        <p>Transform an award-winning Lebanese fine-dining restaurant into a scalable, 
        franchise-ready fast-casual concept for Singapore market domination and 
        international expansion.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>✅ What's Included</h4>
            <ul>
                <li>Complete market research & competitive analysis</li>
                <li>Brand strategy & visual identity system</li>
                <li>Operational blueprint with SOPs</li>
                <li>Franchise system architecture</li>
                <li>3-year rollout plan</li>
                <li>International expansion strategy</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>📈 Market Opportunity</h4>
            <ul>
                <li><b>Market Size:</b> USD 28.92B (2025)</li>
                <li><b>Growth Rate:</b> 18.70% CAGR to 2030</li>
                <li><b>QSR Dominance:</b> 39.4% of profit sector</li>
                <li><b>Target:</b> Urban professionals (25-40 years)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.header("👨‍💼 Strategic Consultant Profile")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>Role</h4>
            <p><b>Strategic Franchise Development Consultant</b></p>
            <p style="color: #666; font-size: 0.9rem;">F&B Sector Specialist</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>Core Competencies</h4>
            <p>✓ Market analysis & competitive intelligence<br>
            ✓ Business model development & financial modeling<br>
            ✓ Brand strategy & operational systems design<br>
            ✓ Franchise architecture & documentation</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Deliverables":
    st.title("📦 Complete Deliverables")
    st.markdown("### All phases completed and delivered")
    
    phases = [
        {
            "phase": "Phase 1: Market Research & Feasibility",
            "duration": "Weeks 1-4 | ~40 hours",
            "items": [
                "Comprehensive Singapore F&B market analysis (USD 28.92B market)",
                "Competitive landscape assessment (direct & indirect competitors)",
                "Target audience persona development (2 primary segments)",
                "Financial feasibility study with break-even analysis"
            ]
        },
        {
            "phase": "Phase 2: Business & Brand Development",
            "duration": "Weeks 5-10 | ~60 hours",
            "items": [
                "Unique Value Proposition (UVP) framework with 3 positioning angles",
                "Menu engineering & pricing strategy (20-25 SKUs)",
                "Complete brand identity package (naming, visual identity, brand story)",
                "Comprehensive business plan (70+ pages, investor-ready)"
            ]
        },
        {
            "phase": "Phase 3: Operational Blueprint",
            "duration": "Weeks 11-24 | ~40 hours",
            "items": [
                "Assembly-line kitchen layout & workflow design",
                "Standard Operating Procedures (SOP) manual",
                "Technology stack recommendations (POS, KDS, CRM)",
                "Supply chain management strategy",
                "Staffing model & training program (4-6 weeks)"
            ]
        },
        {
            "phase": "Phase 4: Franchise System Development",
            "duration": "Weeks 37-48 | ~30 hours",
            "items": [
                "Franchise agreement framework & fee structure",
                "Franchise Operations Manual",
                "Franchisee recruitment & training program",
                "Ongoing support system design",
                "3-year Singapore rollout plan (25-30 stores)",
                "International expansion strategy (Australia, Vietnam)"
            ]
        }
    ]
    
    for i, phase in enumerate(phases, 1):
        with st.expander(f"✅ {phase['phase']}", expanded=(i==1)):
            st.markdown(f"**Duration:** {phase['duration']}")
            st.markdown("**Key Deliverables:**")
            for item in phase['items']:
                st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.success("""
    📄 **Documentation Package:**
    - Business Plan Document 1: 35 pages - Strategic Overview & Market Analysis
    - Business Plan Document 2: 35 pages - Operational Blueprint & Implementation
    - **Total: 120+ pages of comprehensive strategic planning**
    """)

elif page == "Value Proposition":
    st.title("💎 Value Proposition")
    
    st.markdown("""
    <div class="value-highlight">
        <h3>🎯 Why This Matters</h3>
        <p>This isn't just a business plan—it's a complete, franchise-ready system 
        that eliminates years of trial-and-error and positions you for immediate execution.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>📊 Comprehensive Market Intelligence</h4>
            <p>Deep-dive analysis of Singapore's SGD 28.92 billion foodservice market, 
            competitive landscape mapping, and consumer behavior insights.</p>
            <p><b>Standalone Value: SGD 10,000-15,000</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>🎨 Brand Strategy & Identity</h4>
            <p>Complete brand development from positioning through visual identity, 
            connecting authentic Lebanese heritage with modern fast-casual appeal.</p>
            <p><b>Standalone Value: SGD 8,000-12,000</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>🏭 Operational Excellence</h4>
            <p>Detailed operational blueprint with proven assembly-line model, 
            technology integration, supply chain optimization, and labor efficiency strategies.</p>
            <p><b>Standalone Value: SGD 8,000-12,000</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>🤝 Franchise System Architecture</h4>
            <p>Complete franchise framework eliminating 6-12 months of development: 
            legal structure, operations manual, training systems, support structure.</p>
            <p><b>Standalone Value: SGD 15,000-25,000</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📊 Market Rate Comparison")
    
    comparison_data = {
        "Market": ["Singapore Firms", "Regional (APAC)", "India/Philippines", "Your Investment"],
        "Typical Range": ["SGD 25,000 - 40,000", "SGD 15,000 - 25,000", "USD 3,000 - 8,000", "SGD 8,000"],
        "Quality Level": ["High", "Medium-High", "Variable", "Premium"],
        "Your Savings": ["-", "-", "-", "70%"]
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.info("""
    💡 **Total Estimated Market Value:** SGD 35,000 - 50,000
    
    You're receiving premium-quality work at a fraction of market rates, 
    reflecting both geographical arbitrage and our personal relationship.
    """)

elif page == "Investment":
    st.title("💰 Investment Structure")
    
    st.markdown("""
    <div class="price-card">
        <p style="font-size: 1rem; opacity: 0.9; margin: 0;">Total Professional Fee</p>
        <h1 style="font-size: 4rem; margin: 1rem 0;">SGD 8,000</h1>
        <p style="opacity: 0.9;">(approximately USD 6,000)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📊 Pricing Methodology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>Calculation Breakdown</h4>
        </div>
        """, unsafe_allow_html=True)
        
        pricing_data = {
            "Component": [
                "Base Market Rate (Asia-Pacific)",
                "Premium Markup (+50%)",
                "Relationship Discount (-20%)",
                "Final Investment"
            ],
            "Amount (USD)": ["5,000", "7,500", "-1,500", "6,000"],
            "Amount (SGD)": ["-", "-", "-", "8,000"]
        }
        
        df = pd.DataFrame(pricing_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>What This Includes</h4>
            <ul style="margin-top: 0.5rem;">
                <li>~200 hours of strategic consulting work</li>
                <li>Complete 4-phase franchise development</li>
                <li>120+ pages of documentation</li>
                <li>All frameworks, templates & models</li>
                <li>Franchise-ready business plan</li>
                <li>Full rights to all IP & deliverables</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.success("""
    ### 🎁 Relationship Recognition
    
    The 20% discount reflects our long-standing friendship and your support during my 
    challenging times. This pricing balances fair compensation for professional work 
    with genuine appreciation for your help when I needed it.
    """)
    
    st.warning("""
    ### 💡 Payment Flexibility
    
    Given our friendship, I'm completely open to discussing payment terms that work 
    for your situation:
    - Single payment upon acceptance
    - Installment plan (e.g., 50% upfront, 50% within 30 days)
    - Other arrangements aligned with your cash flow
    
    **This is about fairness and partnership, not maximizing fees.**
    """)
    
    st.markdown("---")
    
    st.subheader("💰 Value vs. Market Rates")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Singapore Firms", "SGD 25K-40K", delta="-70% savings")
    with col2:
        st.metric("Regional Firms", "SGD 15K-25K", delta="-60% savings")
    with col3:
        st.metric("Your Investment", "SGD 8K", delta="Premium Quality")

elif page == "Timeline":
    st.title("📅 Project Timeline")
    
    st.success("✅ **All phases completed as of October 2025**")
    
    st.markdown("---")
    
    timeline_data = [
        {"Phase": "Phase 1", "Name": "Market Research & Feasibility", "Duration": "Weeks 1-4", "Status": "✅ Complete"},
        {"Phase": "Phase 2", "Name": "Business & Brand Development", "Duration": "Weeks 5-10", "Status": "✅ Complete"},
        {"Phase": "Phase 3", "Name": "Operational Blueprint", "Duration": "Weeks 11-24", "Status": "✅ Complete"},
        {"Phase": "Phase 4", "Name": "Franchise System Development", "Duration": "Weeks 37-48", "Status": "✅ Complete"}
    ]
    
    for item in timeline_data:
        st.markdown(f"""
        <div class="phase-card">
            <h4>{item['Phase']}: {item['Name']}</h4>
            <p><b>Duration:</b> {item['Duration']} | <b>Status:</b> {item['Status']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🚀 Next Steps for Implementation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>Immediate (Month 1)</h4>
            <ul>
                <li>Review and approve documentation</li>
                <li>Secure initial funding (SGD 2-2.5M)</li>
                <li>Initiate trademark registration</li>
                <li>Begin site reconnaissance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>Short-term (Months 2-6)</h4>
            <ul>
                <li>Location scouting for flagship stores</li>
                <li>Engage franchise legal counsel</li>
                <li>Finalize franchise agreements</li>
                <li>Start supply chain negotiations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("""
    ### 📈 Projected Milestones (Post-Acceptance)
    
    - **Year 1:** Launch 3-4 stores (validate & refine)
    - **Year 2:** Accelerate to 8-10 new stores (franchise rollout begins)
    - **Year 3:** Achieve 25-30 total stores (market saturation)
    - **Year 4+:** International expansion (Australia, Vietnam)
    """)

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
    <h3>Ready to Launch?</h3>
    <p style="color: #666;">This comprehensive franchise development plan provides everything needed to launch 
    and scale your Lebanese fast-casual concept in Singapore and beyond.</p>
    <p style="margin-top: 1rem; font-size: 0.9rem; color: #999;">
        Strategic Franchise Development Consulting | October 2025
    </p>
</div>
""", unsafe_allow_html=True)
```

4. Scroll down and click **"Commit changes"**
5. Click **"Commit changes"** again in the popup

---

### STEP 3: Create `requirements.txt` file

1. Click **"Add file"** → **"Create new file"** again
2. In the "Name your file" box, type: `requirements.txt`
3. **Copy and paste these 2 lines:**
```
streamlit==1.28.0
pandas==2.1.0
