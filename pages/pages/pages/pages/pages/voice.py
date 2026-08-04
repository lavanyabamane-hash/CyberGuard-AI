import streamlit as st
import speech_recognition as sr


st.set_page_config(
    page_title="Voice Threat Analyzer"
)


st.title("🎙️ Voice Threat Analyzer")

st.write(
    "Upload or provide speech input to detect possible phishing threats."
)


audio_file = st.file_uploader(
    "Upload audio file",
    type=["wav"]
)


phishing_keywords = [
    "otp",
    "password",
    "verify",
    "verification",
    "bank",
    "account blocked",
    "account suspended",
    "click here",
    "login",
    "urgent",
    "security alert",
    "confirm identity"
]


def analyze_voice_text(text):

    text_lower = text.lower()

    detected = []

    for word in phishing_keywords:

        if word in text_lower:
            detected.append(word)


    if len(detected) >= 3:

        risk = "🔴 HIGH RISK"

    elif len(detected) > 0:

        risk = "🟡 MEDIUM RISK"

    else:

        risk = "🟢 LOW RISK"


    return risk, detected



def speech_to_text(audio_path):

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:

        audio = recognizer.record(source)


    try:

        text = recognizer.recognize_google(audio)

        return text


    except:

        return "Could not recognize speech"



if audio_file:


    if st.button("🔍 Analyze Voice"):


        with st.spinner("Converting speech to text..."):


            text = speech_to_text(audio_file)


        st.write("## 🛡️ CyberGuard Voice Analysis")


        st.write("### Extracted Speech:")

        st.text(text)



        risk, detected = analyze_voice_text(text)


        st.write("### Risk Level:")


        if "HIGH" in risk:

            st.error(risk)

        elif "MEDIUM" in risk:

            st.warning(risk)

        else:

            st.success(risk)



        st.write("### Detected Threat Keywords:")


        if detected:

            for word in detected:

                st.warning(word)

        else:

            st.success(
                "No suspicious keywords detected."
            )
