import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import requests
import json

plt.style.use('default')
sns.set_palette("husl")

st.set_page_config(
    page_title="Iramiro Business Consulting Firm",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# One Acre Fund color scheme
PRIMARY_GREEN = "#2B7A6D"
LIGHT_GREEN = "#3D9B8F"
DARK_GREEN = "#1F5B52"
ORANGE = "#D84A1B"

st.markdown(f"""
<style>
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Hide default sidebar */
    [data-testid="stSidebar"] {{display: none;}}
    
    /* Compact spacing */
    .block-container {{
        padding-top: 0.3rem;
        padding-bottom: 1rem;
        max-width: 1400px;
    }}
    
    /* Header/Logo - Enhanced */
    .main-header {{
        background: white;
        padding: 1.2rem 2rem;
        border-bottom: 3px solid {PRIMARY_GREEN};
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        position: relative;
    }}
    
    .logo-container {{
        width: 80px;
        height: 80px;
        background: {PRIMARY_GREEN};
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }}
    
    .header-text {{
        flex: 1;
    }}
    
    .logo-text {{
        font-size: 2.2rem;
        font-weight: bold;
        color: {PRIMARY_GREEN};
        margin: 0;
        line-height: 1.2;
    }}
    
    .tagline {{
        font-size: 1.1rem;
        color: {DARK_GREEN};
        margin: 0.3rem 0 0 0;
        font-style: italic;
    }}
    
    /* Navigation - LARGER AND CLEARER */
    .stButton > button {{
        background-color: white;
        color: {PRIMARY_GREEN};
        border: 2px solid {PRIMARY_GREEN};
        border-radius: 8px;
        padding: 1rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 700;
        transition: all 0.3s;
        height: 60px;
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }}
    
    .stButton > button:hover {{
        background-color: {PRIMARY_GREEN};
        color: white;
        border-color: {PRIMARY_GREEN};
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}
    
    /* Service Cards - Compact */
    .service-card {{
        background: {LIGHT_GREEN};
        padding: 1rem;
        border-radius: 6px;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    
    .service-card h3 {{
        font-size: 1.1rem;
        margin: 0 0 0.5rem 0;
    }}
    
    /* Expert Cards - Horizontal & Compact */
    .expert-card {{
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 6px;
        margin: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {PRIMARY_GREEN};
        min-height: 200px;
    }}
    
    .expert-name {{
        font-size: 1.1rem;
        font-weight: bold;
        color: {PRIMARY_GREEN};
        margin-bottom: 0.3rem;
    }}
    
    .expert-title {{
        font-size: 0.9rem;
        color: {DARK_GREEN};
        margin-bottom: 0.5rem;
    }}
    
    /* Impact boxes - Compact */
    .impact-box {{
        background: {PRIMARY_GREEN};
        padding: 1rem;
        border-radius: 6px;
        color: white;
        text-align: center;
        margin: 0.3rem 0;
    }}
    
    .stat-number {{
        font-size: 1.8rem;
        font-weight: bold;
        margin: 0;
    }}
    
    .stat-label {{
        font-size: 0.85rem;
        margin: 0;
        opacity: 0.9;
    }}
    
    /* Testimonials - Compact */
    .testimonial-box {{
        background-color: #FFF8E1;
        padding: 1rem;
        border-radius: 6px;
        border-left: 3px solid {ORANGE};
        margin: 0.5rem 0;
        font-style: italic;
        font-size: 0.9rem;
    }}
    
    /* Footer - Compact */
    .footer {{
        background-color: {DARK_GREEN};
        color: white;
        padding: 1.5rem;
        margin-top: 2rem;
        border-radius: 6px;
        text-align: center;
    }}
    
    .footer-info {{
        font-size: 0.95rem;
        line-height: 1.8rem;
    }}
    
    /* AI Chat - MOVED TO BOTTOM */
    .chat-container {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 380px;
        max-height: 500px;
        background: white;
        border: 3px solid {PRIMARY_GREEN};
        border-radius: 15px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        z-index: 999;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }}
    
    .chat-header {{
        background: {PRIMARY_GREEN};
        color: white;
        padding: 1rem;
        font-weight: bold;
        font-size: 1.1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    
    .chat-messages {{
        flex: 1;
        overflow-y: auto;
        padding: 1rem;
        max-height: 300px;
    }}
    
    .chat-input-area {{
        border-top: 2px solid {PRIMARY_GREEN};
        padding: 1rem;
        background: #f8f9fa;
    }}
    
    .chat-toggle {{
        position: fixed;
        right: 20px;
        bottom: 20px;
        z-index: 998;
        background: {PRIMARY_GREEN};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 50px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        font-weight: bold;
        font-size: 1rem;
        border: none;
    }}
    
    .chat-toggle:hover {{
        background: {DARK_GREEN};
        transform: scale(1.05);
    }}
    
    .chat-message {{
        margin: 0.8rem 0;
        padding: 0.8rem;
        border-radius: 12px;
        font-size: 0.95rem;
        line-height: 1.4;
    }}
    
    .user-message {{
        background-color: {LIGHT_GREEN};
        color: white;
        margin-left: 15%;
    }}
    
    .bot-message {{
        background-color: #e9ecef;
        color: #333;
        margin-right: 15%;
    }}
    
    /* Form styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {{
        border-color: {PRIMARY_GREEN};
        font-size: 0.9rem;
    }}
    
    /* Compact headings */
    h1 {{
        font-size: 2rem;
        color: {PRIMARY_GREEN};
        margin-top: 0;
        margin-bottom: 0.5rem;
    }}
    
    h2 {{
        font-size: 1.5rem;
        color: {PRIMARY_GREEN};
        margin-bottom: 0.5rem;
    }}
    
    h3 {{
        font-size: 1.2rem;
        color: {DARK_GREEN};
        margin-bottom: 0.5rem;
    }}
    
    /* Info/Success boxes - compact */
    .stAlert {{
        padding: 0.8rem;
        font-size: 0.9rem;
    }}
</style>
""", unsafe_allow_html=True)

# Google Sheets integration function
def submit_to_google_sheets(data):
    """Submit form data to Google Sheets"""
    try:
        # Google Sheets webhook URL (you'll need to set this up with Google Apps Script)
        # For now, we'll return True to simulate success
        # You need to create a Google Apps Script web app that accepts POST requests
        
        # Example Apps Script code needed:
        """
        function doPost(e) {
          var sheet = SpreadsheetApp.openById('1Duh5svqqT2NTvKIetwaYUA6QRs_p0gRyS_OnQpx-axI').getActiveSheet();
          var data = JSON.parse(e.postData.contents);
          sheet.appendRow([
            new Date(),
            data.company_name,
            data.industry,
            data.company_size,
            data.contact_name,
            data.email,
            data.position,
            data.phone,
            data.services,
            data.preferred_expert,
            data.preferred_date,
            data.preferred_time,
            data.meeting_type,
            data.message
          ]);
          return ContentService.createTextOutput(JSON.stringify({result: 'success'}))
            .setMimeType(ContentService.MimeType.JSON);
        }
        """
        
        # For demonstration, we'll log the data
        # In production, replace with your Google Apps Script webhook URL
        # webhook_url = "YOUR_GOOGLE_APPS_SCRIPT_WEBHOOK_URL"
        # response = requests.post(webhook_url, json=data)
        
        return True
    except Exception as e:
        st.error(f"Error submitting to Google Sheets: {str(e)}")
        return False

# Session state
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home"

if 'chat_open' not in st.session_state:
    st.session_state.chat_open = False

if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "bot", "content": "Hello! 👋 I'm your AI assistant. I can help you with:\n\n• Expansion strategies & market opportunities\n• Service information & pricing\n• Expert consultations\n• Regional growth planning\n\nHow can I help you today?"}
    ]

# Stats
@st.cache_data
def get_impact_stats():
    return {
        'clients_served': 150,
        'projects_completed': 280,
        'satisfaction_rate': 96,
        'years_experience': 15,
        'successful_audits': 120,
        'tax_savings': 45000000,
        'businesses_grown': 85,
        'market_expansions': 42
    }

stats = get_impact_stats()

# ENHANCED AI Response function with expansion planning capabilities
def get_ai_response(user_message):
    message_lower = user_message.lower()
    
    # Expansion-related queries
    if any(word in message_lower for word in ['expan', 'grow', 'scale', 'new market', 'branch']):
        return """🚀 **Expansion Opportunities for Rwanda:**

**Regional Markets:**
• East African Community (EAC) - Kenya, Tanzania, Uganda
• DRC - High demand for professional services
• Burundi - Emerging consulting market

**Service Expansion:**
• Digital transformation consulting
• ESG & sustainability advisory
• Tech startup advisory services

**Sectors to Target:**
• Tech companies (fastest growing)
• Agriculture (largest sector)
• Real estate & construction

Would you like specific strategies for any of these opportunities?"""
    
    # Strategic planning
    elif any(word in message_lower for word in ['strateg', 'plan', 'roadmap']):
        return """📋 **Strategic Expansion Planning:**

**Phase 1 (0-6 months):**
• Market research in target countries
• Partnership identification
• Service customization

**Phase 2 (6-12 months):**
• Pilot projects in new markets
• Local expert recruitment
• Brand establishment

**Phase 3 (12-24 months):**
• Full market entry
• Branch office setup
• Scale operations

I can help you develop a detailed roadmap. What's your timeline?"""
    
    # Market opportunities
    elif any(word in message_lower for word in ['opportunit', 'market', 'sector']):
        return """💡 **Key Market Opportunities:**

**High-Growth Sectors:**
1. **Tech & Innovation** - 40% annual growth
2. **Agribusiness** - Export potential
3. **Tourism & Hospitality** - Recovery phase
4. **Manufacturing** - Government incentives

**Underserved Areas:**
• Secondary cities (Huye, Rubavu, Musanze)
• SME sector consulting
• Cross-border trade advisory

**Emerging Needs:**
• Compliance for foreign investors
• Digital transformation
• Sustainability reporting

Which sector interests you most?"""
    
    # Service-related queries
    elif any(word in message_lower for word in ['service', 'services', 'offer']):
        return """💼 **Our Services:**

📋 **Auditing & Assurance** - Financial audits, compliance
💰 **Taxation Services** - Planning, filing, optimization
📊 **Business Analysis** - Market research, strategic planning
🎯 **Business Development** - Growth strategies, operations

**Expansion-Specific Services:**
• Market entry strategy
• Feasibility studies
• Partnership facilitation
• Regulatory compliance

Which service interests you?"""
    
    # Pricing queries
    elif any(word in message_lower for word in ['price', 'cost', 'fee', 'budget']):
        return """💰 **Investment & Pricing:**

**Free Consultation:** Initial 30-min assessment
**Feasibility Study:** RWF 2-5M (depending on scope)
**Market Entry Strategy:** RWF 5-10M
**Full Expansion Package:** Custom quote

**ROI Focus:**
• 150+ successful projects
• Average 40% efficiency gains
• RWF 45M+ in client tax savings

Book a free consultation: +250 787897647"""
    
    # Contact queries
    elif any(word in message_lower for word in ['contact', 'email', 'phone', 'meet']):
        return """📞 **Contact Us:**

📧 Email: info@rwandaconsulting.rw
📱 Phone: +250 787897647
📍 Office: Kimironko, Kigali

**Meeting Options:**
• In-person consultation (Free)
• Video call (Zoom/Teams)
• Phone consultation

**Response Time:** Within 24 hours

Click 'Contact' above to schedule!"""
    
    # Expert queries
    elif any(word in message_lower for word in ['expert', 'team', 'consultant', 'advisor']):
        return """👥 **Our Expert Team:**

**Richard Ngarukiyintwari** (CPA)
• Audit & Tax specialist
• 15+ years experience
• 120+ successful audits

**Gerard Ndagijimana** (MBA)
• Business Analysis & Operations
• 12+ years experience
• 85+ businesses transformed

**Cedric Irambona** (MSc)
• Business Development
• 10+ years experience
• 42 market expansions led

Check 'Our Experts' page for details!"""
    
    # Regional expansion
    elif any(word in message_lower for word in ['region', 'eac', 'kenya', 'tanzania', 'uganda', 'drc']):
        return """🌍 **Regional Expansion Insights:**

**Easiest Markets:**
• Kenya - Largest economy, established infrastructure
• Tanzania - Growing SME sector
• Uganda - English-speaking, similar regulations

**High-Potential:**
• DRC - Massive market, limited competition
• Burundi - Emerging opportunities

**Success Factors:**
• Local partnerships (essential)
• Regulatory compliance expertise
• Cultural adaptation

Want a detailed regional strategy?"""
    
    # Greetings
    elif any(word in message_lower for word in ['hello', 'hi', 'hey', 'good']):
        return """Hello! 👋 Welcome to Iramiro Business Consulting.

I'm here to help with:
🚀 Expansion planning & opportunities
💼 Service information
👥 Expert consultations
📊 Market insights

What would you like to know?"""
    
    # Thank you
    elif any(word in message_lower for word in ['thank', 'thanks', 'appreciate']):
        return "You're welcome! 😊 Feel free to ask anything else. I'm here to help you succeed!"
    
    # Default response
    else:
        return """I can help you with:

🚀 **Expansion & Growth** - Markets, strategies, roadmaps
💼 **Services** - Audit, tax, analysis, development
💰 **Pricing** - Packages, ROI, investment
👥 **Experts** - Team capabilities, experience
📞 **Contact** - Schedule consultations

What specific information do you need?"""

# Header with Logo
# Note: Place 'iramiro_logo.png' in the same directory as this script
import base64
from pathlib import Path

# Function to load logo
def get_logo_base64():
    logo_path = Path(__file__).parent / "iramiro_logo.png"
    if logo_path.exists():
        with open(logo_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_logo_base64()

if logo_b64:
    st.markdown(f"""
    <div class="main-header">
        <img src="data:image/png;base64,{logo_b64}" style="width: 80px; height: 80px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.15);">
        <div class="header-text">
            <h1 class="logo-text">Iramiro Business Consulting Firm</h1>
            <p class="tagline">Your Partner in Business Excellence and Growth</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="main-header">
        <div class="logo-container">
            🎯
        </div>
        <div class="header-text">
            <h1 class="logo-text">Iramiro Business Consulting Firm</h1>
            <p class="tagline">Your Partner in Business Excellence and Growth</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# AI Chat button using Streamlit but positioned in header
col1, col2 = st.columns([11, 1])
with col2:
    if st.button("AI Chat", key="toggle_chat"):
        st.session_state.chat_open = not st.session_state.chat_open
        st.rerun()

# LARGER Navigation
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "🏠 Home"
with col2:
    if st.button("ℹ️ About Us", use_container_width=True):
        st.session_state.page = "ℹ️ About Us"
with col3:
    if st.button("💼 Services", use_container_width=True):
        st.session_state.page = "💼 Services"
with col4:
    if st.button("👥 Our Experts", use_container_width=True):
        st.session_state.page = "👥 Experts"
with col5:
    if st.button("📊 Impact", use_container_width=True):
        st.session_state.page = "📊 Impact"
with col6:
    if st.button("📞 Contact", use_container_width=True):
        st.session_state.page = "📞 Contact"

# Position AI Chat button in header
st.markdown("""
<style>
    /* Move AI Chat button column up into header - above green line */
    div[data-testid="column"]:nth-child(2):has(button[key="toggle_chat"]) {
        position: absolute;
        right: 2rem;
        top: 1.5rem;
        z-index: 1000;
    }
    
    /* Style the AI Chat button */
    button[key="toggle_chat"] {
        background-color: white !important;
        color: #2B7A6D !important;
        border: 2px solid #2B7A6D !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.5rem !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
        height: auto !important;
    }
    
    button[key="toggle_chat"]:hover {
        background-color: #2B7A6D !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

page = st.session_state.page

# AI Chat - Bottom Right Corner
if st.session_state.chat_open:
    st.markdown("""
    <div class="chat-container">
        <div class="chat-header">
            🤖 AI Business Advisor
            <span style="cursor: pointer;" onclick="this.parentElement.parentElement.style.display='none'">✖</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a container for chat
    chat_container = st.container()
    
    with chat_container:
        # Display messages
        for message in st.session_state.chat_messages:
            if message["role"] == "bot":
                st.markdown(f'<div class="chat-message bot-message">🤖 {message["content"]}</div>', 
                           unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message user-message">👤 {message["content"]}</div>', 
                           unsafe_allow_html=True)
        
        # Chat input area
        col1, col2 = st.columns([4, 1])
        with col1:
            user_input = st.text_input("Type your message...", key="chat_input", label_visibility="collapsed")
        with col2:
            send_btn = st.button("Send", key="send_chat", use_container_width=True)
        
        if send_btn and user_input:
            st.session_state.chat_messages.append({"role": "user", "content": user_input})
            response = get_ai_response(user_input)
            st.session_state.chat_messages.append({"role": "bot", "content": response})
            st.rerun()

# HOME PAGE
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("# Transform Your Business")
        st.markdown("""
        We provide comprehensive business solutions tailored to Rwanda's dynamic market. 
        From auditing and taxation to business development and operational excellence.
        
        **Why Choose Us?**
        - ✅ Local Expertise & Proven Track Record
        - ✅ 150+ Satisfied Clients | 96% Satisfaction Rate
        - ✅ Certified Professionals with 15+ Years Experience
        - ✅ Regional Expansion Specialists (EAC, DRC)
        """)
        
        if st.button("📞 Get Free Consultation", key="hero_cta", type="primary"):
            st.session_state.page = "📞 Contact"
            st.rerun()
    
    with col2:
        st.markdown(f'<div class="impact-box"><p class="stat-number">150+</p><p class="stat-label">Clients</p></div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="impact-box"><p class="stat-number">96%</p><p class="stat-label">Satisfaction</p></div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="impact-box"><p class="stat-number">280+</p><p class="stat-label">Projects</p></div>', 
                   unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## 🚀 Our Services")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📋 Auditing & Assurance**  
        Financial audits, compliance reviews, and internal controls
        
        **💰 Taxation Services**  
        Tax planning, filing, and compliance optimization
        """)
    
    with col2:
        st.markdown("""
        **📊 Business Analysis**  
        Market research, strategic planning, and analysis
        
        **🎯 Business Development**  
        Growth strategies and operational excellence
        """)
    
    st.markdown("---")
    st.markdown("## 💬 Client Testimonials")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="testimonial-box">
        "Professional audit team. Helped us achieve full compliance."
        <br><strong>- John M., TechStart</strong>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="testimonial-box">
        "40% efficiency increase in 6 months. Outstanding results!"
        <br><strong>- Grace U., GreenAgri</strong>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="testimonial-box">
        "Saved RWF 5M+ in taxes. Excellent service!"
        <br><strong>- Eric N., BuildRight</strong>
        </div>
        """, unsafe_allow_html=True)

# ABOUT US PAGE
elif page == "ℹ️ About Us":
    st.markdown("# About Iramiro Business Consulting")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Our Story
        Founded in 2009, we've been transforming Rwandan businesses for over 15 years. 
        From a small auditing practice to a comprehensive consulting firm serving 150+ clients.
        
        ## Our Mission
        To empower Rwandan businesses with expert consulting that drives growth, ensures compliance, 
        and builds sustainable success across East Africa.
        
        ## Our Values
        **🎯 Excellence** | **🤝 Integrity** | **💡 Innovation** | **🌱 Growth** | **🇷🇼 Local Commitment**
        """)
    
    with col2:
        st.markdown(f'<div class="impact-box"><p class="stat-number">2009</p><p class="stat-label">Founded</p></div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="impact-box"><p class="stat-number">15+</p><p class="stat-label">Years</p></div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="impact-box"><p class="stat-number">150+</p><p class="stat-label">Clients</p></div>', 
                   unsafe_allow_html=True)

# SERVICES PAGE
elif page == "💼 Services":
    st.markdown("# Our Services")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="service-card">
        <h3>📋 Auditing & Assurance</h3>
        <p>Financial audits, internal audits, compliance reviews, forensic audits, due diligence</p>
        <p><strong>Expert: Richard Ngarukiyintwari (CPA)</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="service-card">
        <h3>📊 Business Analysis</h3>
        <p>Market research, strategic planning, financial analysis, investment analysis</p>
        <p><strong>Expert: Gerard Ndagijimana (MBA)</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="service-card">
        <h3>💰 Taxation Services</h3>
        <p>Tax planning, compliance, VAT services, transfer pricing, dispute resolution</p>
        <p><strong>Expert: Richard Ngarukiyintwari (CPA)</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="service-card">
        <h3>🎯 Business Development</h3>
        <p>Growth strategy, market expansion, operations management, process optimization</p>
        <p><strong>Experts: Gerard N. & Cedric I.</strong></p>
        </div>
        """, unsafe_allow_html=True)

# EXPERTS PAGE
elif page == "👥 Experts":
    st.markdown("# Meet Our Expert Team")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="expert-card">
        <div class="expert-name">Richard Ngarukiyintwari</div>
        <div class="expert-title">Senior Auditor & Tax Consultant</div>
        <p style="font-size: 0.85rem; margin: 0.5rem 0;">
        <strong>Specializations:</strong><br>
        • Financial Auditing<br>
        • Tax Planning & Compliance<br>
        • Forensic Accounting<br>
        • Regulatory Compliance
        </p>
        <p style="font-size: 0.85rem; margin: 0.5rem 0;">
        <strong>Qualifications:</strong><br>
        CPA, Chartered Tax Advisor<br>
        15+ years experience
        </p>
        <p style="font-size: 0.85rem; margin-top: 0.5rem;">
        <em>120+ successful audits completed</em>
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="expert-card">
        <div class="expert-name">Gerard Ndagijimana</div>
        <div class="expert-title">Business Analyst & Operations Manager</div>
        <p style="font-size: 0.85rem; margin: 0.5rem 0;">
        <strong>Specializations:</strong><br>
        • Business Analysis<br>
        • Operations Management<br>
        • Process Optimization<br>
        • Strategic Planning
        </p>
        <p style="font-size: 0.85rem; margin: 0.5rem 0;">
        <strong>Qualifications:</strong><br>
        MBA, CBAP, Six Sigma Black Belt<br>
        12+ years experience
        </p>
        <p style="font-size: 0.85rem; margin-top: 0.5rem;">
        <em>85+ businesses transformed</em>
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="expert-card">
        <div class="expert-name">Cedric Irambona</div>
        <div class="expert-title">Business Development Specialist</div>
        <p style="font-size: 0.85rem; margin: 0.5rem 0;">
        <strong>Specializations:</strong><br>
        • Business Development<br>
        • Market Expansion<br>
        • Strategic Partnerships<br>
        • Sales Optimization
        </p>
        <p style="font-size: 0.85rem; margin: 0.5rem 0;">
        <strong>Qualifications:</strong><br>
        MSc Business Development<br>
        10+ years experience
        </p>
        <p style="font-size: 0.85rem; margin-top: 0.5rem;">
        <em>42 market expansions led</em>
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 🏆 Collective Impact")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="impact-box"><p class="stat-number">15+</p><p class="stat-label">Avg Years Exp</p></div>', 
                   unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="impact-box"><p class="stat-number">150+</p><p class="stat-label">Clients</p></div>', 
                   unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="impact-box"><p class="stat-number">280+</p><p class="stat-label">Projects</p></div>', 
                   unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="impact-box"><p class="stat-number">96%</p><p class="stat-label">Satisfaction</p></div>', 
                   unsafe_allow_html=True)

# IMPACT PAGE
elif page == "📊 Impact":
    st.markdown("# Our Impact")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f'<div class="impact-box"><p class="stat-number">{stats["clients_served"]}+</p><p class="stat-label">Clients</p></div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="impact-box"><p class="stat-number">{stats["projects_completed"]}+</p><p class="stat-label">Projects</p></div>', 
                   unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="impact-box"><p class="stat-number">{stats["satisfaction_rate"]}%</p><p class="stat-label">Satisfaction</p></div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="impact-box"><p class="stat-number">{stats["years_experience"]}+</p><p class="stat-label">Years Exp</p></div>', 
                   unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'<div class="impact-box"><p class="stat-number">RWF {stats["tax_savings"]/1000000:.0f}M+</p><p class="stat-label">Tax Savings</p></div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="impact-box"><p class="stat-number">{stats["market_expansions"]}+</p><p class="stat-label">Expansions</p></div>', 
                   unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 📈 Growth Metrics")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    
    years = [2020, 2021, 2022, 2023, 2024]
    clients = [20, 35, 55, 90, 150]
    ax1.plot(years, clients, marker='o', linewidth=2, markersize=8, color=PRIMARY_GREEN)
    ax1.fill_between(years, clients, alpha=0.3, color=PRIMARY_GREEN)
    ax1.set_title('Client Growth', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Clients')
    ax1.grid(True, alpha=0.3)
    
    services = ['Audit', 'Tax', 'Analysis', 'Dev']
    service_clients = [45, 38, 35, 32]
    ax2.bar(services, service_clients, color=PRIMARY_GREEN, alpha=0.8)
    ax2.set_title('Services Distribution', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Clients')
    ax2.grid(True, alpha=0.3, axis='y')
    
    satisfaction = [94, 95, 98, 97]
    ax3.barh(services, satisfaction, color=LIGHT_GREEN, alpha=0.8)
    ax3.set_title('Satisfaction by Service (%)', fontsize=11, fontweight='bold')
    ax3.set_xlim(90, 100)
    ax3.grid(True, alpha=0.3)
    
    metrics = ['On Time', 'In Budget', 'Exceeded', 'Repeat']
    percentages = [95, 92, 88, 78]
    ax4.bar(metrics, percentages, color=ORANGE, alpha=0.8)
    ax4.set_title('Success Metrics (%)', fontsize=11, fontweight='bold')
    ax4.set_ylim(0, 100)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# CONTACT PAGE
elif page == "📞 Contact":
    st.markdown("# Contact Us")
    st.markdown("Let's discuss how we can help your business succeed")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("contact_form"):
            col_a, col_b = st.columns(2)
            
            with col_a:
                company_name = st.text_input("Company Name *", placeholder="Your Company Ltd")
                contact_name = st.text_input("Full Name *", placeholder="John Doe")
                email = st.text_input("Email *", placeholder="john@company.com")
            
            with col_b:
                industry = st.selectbox("Industry *", ["Select", "Technology", "Agriculture", "Manufacturing", 
                                                       "Retail", "Finance", "Healthcare", "Other"])
                position = st.text_input("Position *", placeholder="CEO/Manager")
                phone = st.text_input("Phone *", placeholder="+250 788 123 456")
            
            company_size = st.selectbox("Company Size *", ["Select", "1-10", "11-50", "51-200", "200+"])
            
            services_needed = st.multiselect("Services Interested In *", 
                                            ["Auditing", "Taxation", "Business Analysis", "Business Development", "Expansion Planning"])
            
            preferred_expert = st.selectbox("Preferred Expert", 
                                           ["No Preference", "Richard (Audit/Tax)", "Gerard (Analysis/Ops)", "Cedric (Development)"])
            
            col_c, col_d = st.columns(2)
            with col_c:
                preferred_date = st.date_input("Preferred Date *", min_value=datetime.now().date())
            with col_d:
                preferred_time = st.selectbox("Preferred Time *", 
                                             ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"])
            
            meeting_type = st.radio("Meeting Type *", ["In-Person (Kimironko)", "Video Call", "Phone Call"])
            
            message = st.text_area("Message *", placeholder="How can we help you?", height=100)
            
            submitted = st.form_submit_button("📧 Submit Request", use_container_width=True, type="primary")
            
            if submitted:
                if not all([company_name, contact_name, email, phone, message]) or industry == "Select" or company_size == "Select" or not services_needed:
                    st.error("❌ Please fill all required fields (*)")
                elif "@" not in email:
                    st.error("❌ Please enter a valid email")
                else:
                    form_data = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "company_name": company_name,
                        "industry": industry,
                        "company_size": company_size,
                        "contact_name": contact_name,
                        "email": email,
                        "position": position,
                        "phone": phone,
                        "services": ", ".join(services_needed),
                        "preferred_expert": preferred_expert,
                        "preferred_date": str(preferred_date),
                        "preferred_time": preferred_time,
                        "meeting_type": meeting_type,
                        "message": message
                    }
                    
                    success = submit_to_google_sheets(form_data)
                    
                    if success:
                        st.success(f"""
                        ✅ **Request Submitted Successfully!**
                        
                        We'll contact you within 24 hours at: {email}
                        
                        **Need immediate help?** Call +250 787897647
                        """)
                        
                        st.info(f"""
                        **Summary:** {company_name} | {contact_name} | {', '.join(services_needed)} | {preferred_date}
                        """)
    
    with col2:
        st.markdown("### 📍 Our Office")
        st.info("""
        **Location:**  
        Kigali - Kimironko, Rwanda
        
        **Email:**  
        info@rwandaconsulting.rw
        
        **Phone:**  
        +250 787897647
        
        **Hours:**  
        Mon-Fri: 8AM-6PM  
        Sat: 9AM-1PM
        """)
        
        st.success("""
        ✅ Free Consultation  
        ✅ Expert Guidance  
        ✅ No Obligation  
        ✅ 24hr Response
        """)

# FOOTER
st.markdown("---")
st.markdown(f"""
<div class="footer">
    <h3 style="color: {LIGHT_GREEN}; margin-bottom: 0.5rem;">🎯 Iramiro Business Consulting Firm</h3>
    <div class="footer-info">
        <p><strong>📍 Address:</strong> Kigali - Kimironko, Rwanda</p>
        <p><strong>📞 Phone:</strong> +250 787897647</p>
        <p><strong>📧 Email:</strong> info@rwandaconsulting.rw</p>
    </div>
    <p style="margin-top: 1rem; font-size: 0.85rem; opacity: 0.8;">
    &copy; 2025 Iramiro Business Consulting Firm. All rights reserved.<br>
    <em>Your Partner in Business Excellence and Growth</em>
    </p>
</div>
""", unsafe_allow_html=True)