import streamlit as st
import os
import time
from streamlit_option_menu import option_menu
from streamlit_mic_recorder import mic_recorder

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(
    page_title="VeeraMotion AI | Innovation Studio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED CSS (GSAP & Glassmorphism Inspired) ---
st.markdown("""
    <style>
    /* Dark Futuristic Background */
    .stApp {
        background: radial-gradient(circle at top right, #001a33, #000000);
        color: #e0f7fa;
    }
    
    /* Smooth Entrance Animation */
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Glassmorphism Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 242, 255, 0.2);
        padding: 25px;
        border-radius: 20px;
        animation: slideUp 0.8s ease-out;
        transition: 0.3s ease;
    }
    .feature-card:hover {
        border: 1px solid #00f2ff;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.2);
    }

    /* Neon Titles */
    .neon-title {
        font-family: 'Inter', sans-serif;
        font-size: 50px;
        font-weight: 800;
        background: linear-gradient(90deg, #00f2ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #000814;
        border-right: 1px solid rgba(0, 242, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION MANAGEMENT ---
if 'auth_state' not in st.session_state:
    st.session_state.auth_state = False

# --- 4. NEURAL GATEWAY (LOGIN) ---
if not st.session_state.auth_state:
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="feature-card" style="text-align:center;">', unsafe_allow_html=True)
        st.markdown('<h1 style="color:#00f2ff;">VEERAMOTION GATEWAY</h1>', unsafe_allow_html=True)
        st.write("Enter Credentials to Access Studio")
        
        u_id = st.text_input("CREATOR IDENTITY", placeholder="Learnomine_Creator")
        u_key = st.text_input("NEURAL KEY", type="password", placeholder="CHAT_AI_2026")
        
        if st.button("INITIALIZE STUDIO"):
            if u_id == "Learnomine_Creator" and u_key == "CHAT_AI_2026":
                with st.spinner("Synchronizing UI Layers..."):
                    time.sleep(1.5)
                st.session_state.auth_state = True
                st.rerun()
            else:
                st.error("Access Denied. Check your Neural Key.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 5. MAIN STUDIO NAVIGATION ---
with st.sidebar:
    st.markdown("### 🛠️ Control Panel")
    selected = option_menu(
        "VeeraMotion", ["Studio Home", "Vocal Neural Link", "InnoVation Lab", "Contact"],
        icons=['house', 'mic', 'cpu', 'envelope'],
        menu_icon="robot", default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "nav-link-selected": {"background-color": "#0072ff"}
        }
    )
    if st.button("Exit System"):
        st.session_state.auth_state = False
        st.rerun()

# --- 6. ADVANCED STUDIO SECTIONS ---

if selected == "Studio Home":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        # Photo Error Handling
        img_file = "image_e5496b.jpg"
        if os.path.exists(img_file):
            st.image(img_file, width=320, use_container_width=False)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/8727/8727604.png", width=250)
            st.warning("⚠️ Photo missing in GitHub. Please upload 'image_e5496b.jpg'.")

    with col2:
        st.markdown('<h1 class="neon-title">Veerababu</h1>', unsafe_allow_html=True)
        st.subheader("AI Developer & UI Innovation Designer")
        st.write("""
            Welcome to **VeeraMotion AI Studio**. I specialize in creating interactive 
            web experiences using **HTML/CSS/JS/GSAP** and integrating them with 
            cutting-edge **AI technologies**.
        """)
        st.markdown("""
            - **Tech Stack:** Python, Streamlit, GSAP, Java, NLP
            - **Mission:** Bridging the gap between fluid design and neural logic.
        """)
        st.button("Download Neural Portfolio")

elif selected == "Vocal Neural Link":
    st.title("🎙️ Vocal Neural Interface")
    st.write("Experience seamless Voice-to-Command technology.")
    
    col_l, col_r = st.columns([1, 2])
    with col_l:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.write("Recording Node")
        audio = mic_recorder(start_prompt="🎤 Start Listening", stop_prompt="🛑 End Stream", key='v_rec')
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_r:
        if audio:
            st.success("Signal Captured!")
            st.json({"Status": "Success", "Latency": "14ms", "Mode": "Vocal"})
            st.chat_message("assistant").write("Hello Veerababu, I have received your neural voice signal. How can I assist you in the studio today?")
        else:
            st.chat_input("Type a command for VeeraMotion...")

elif selected == "InnoVation Lab":
    st.title("🧪 InnoVation Design Lab")
    st.write("Testing GSAP-inspired interactive modules.")
    
    tab1, tab2 = st.tabs(["Design Patterns", "AI Logic"])
    with tab1:
        st.markdown('<div class="feature-card"><h3>Fluid UI Components</h3><p>Integrating GSAP scroll triggers with Streamlit backend.</p></div>', unsafe_allow_html=True)
    with tab2:
        st.write("Neural Classification System Active.")
        st.progress(85, text="Model Training Accuracy")

st.markdown("---")
st.caption("VeeraMotion AI V3.0 | 2026 | Powered by Veerababu Innovation Studio")
