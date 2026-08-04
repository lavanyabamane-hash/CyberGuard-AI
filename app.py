import streamlit as st


st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)


# Sidebar

st.sidebar.title("🛡️ CyberGuard AI")

st.sidebar.write(
    """
    ### Modules

    🖼️ Image Analysis  
    🔐 Password Security  
    🎣 Phishing Detector  
    🎙️ Voice Threat Analyzer  
    🤖 AI Cyber Assistant
    """
)

st.sidebar.divider()

st.sidebar.info(
    "Stay Safe. Stay Cyber Aware."
)



# Main Page

st.title("🛡️ CyberGuard AI")

st.subheader(
    "AI-Powered Cybersecurity Assistant"
)


st.write(
    """
    CyberGuard AI is an intelligent cybersecurity platform that helps users
    identify cyber threats, analyze suspicious content, and improve digital safety.
    """
)


st.divider()



# Features Section

st.header("🚀 Features")


col1, col2 = st.columns(2)



with col1:

    st.subheader("🖼️ Image Analysis")

    st.write(
        """
        • Extracts text from images using OCR  
        • Detects phishing-related content  
        • Provides risk classification
        """
    )


    st.subheader("🔐 Password Security")

    st.write(
        """
        • Checks password strength  
        • Gives security recommendations  
        • Calculates security score
        """
    )


    st.subheader("🎣 Phishing Detection")

    st.write(
        """
        • Analyzes suspicious messages  
        • Detects scam indicators  
        • Provides safety advice
        """
    )



with col2:

    st.subheader("🎙️ Voice Threat Analyzer")

    st.write(
        """
        • Converts speech into text  
        • Detects suspicious voice messages  
        • Identifies cyber threats
        """
    )


    st.subheader("🤖 AI Cyber Assistant")

    st.write(
        """
        • Answers cybersecurity questions  
        • Provides awareness tips  
        • Powered by AI
        """
    )



st.divider()



# Working Flow

st.header("⚙️ How CyberGuard AI Works")


st.write(
    """
    1. User provides input (image, message, password, voice, or question)

    2. AI-based analysis processes the information

    3. CyberGuard AI identifies possible risks

    4. The system provides security recommendations
    """
)



st.divider()



# Cyber Safety Tips

st.header("🛡️ Cyber Safety Tips")


tips = [
    "Never share OTPs or passwords with anyone.",
    "Avoid clicking unknown links.",
    "Use strong and unique passwords.",
    "Enable two-factor authentication.",
    "Verify suspicious messages before responding."
]


for tip in tips:

    st.success(tip)



st.divider()



st.caption(
    "CyberGuard AI | AI-based Cybersecurity Awareness Platform"
)
