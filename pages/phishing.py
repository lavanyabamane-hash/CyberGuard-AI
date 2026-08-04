import streamlit as st


st.set_page_config(
    page_title="Phishing Detector"
)


st.title("🎣 Phishing Message Detector")

st.write(
    "Analyze suspicious messages, SMS, emails, or chats for phishing indicators."
)


message = st.text_area(
    "Paste suspicious message here:"
)


# Common phishing indicators
phishing_keywords = [
    "otp",
    "password",
    "verify",
    "verification",
    "verify your account",
    "click here",
    "urgent",
    "immediately",
    "account suspended",
    "account blocked",
    "bank",
    "login",
    "confirm identity",
    "claim",
    "winner",
    "prize",
    "free",
    "offer",
    "reward",
    "security alert"
]


def analyze_phishing(text):

    text_lower = text.lower()

    detected_keywords = []


    for word in phishing_keywords:

        if word in text_lower:
            detected_keywords.append(word)


    # Risk calculation

    if len(detected_keywords) >= 4:

        risk = "🔴 HIGH RISK"

    elif len(detected_keywords) >= 2:

        risk = "🟡 MEDIUM RISK"

    else:

        risk = "🟢 LOW RISK"


    return risk, detected_keywords



if st.button("🔍 Analyze Message"):


    if message.strip():


        risk, detected = analyze_phishing(message)


        st.write("## 🛡️ CyberGuard Analysis")


        st.write(
            "Risk Level:"
        )

        if "HIGH" in risk:

            st.error(risk)

        elif "MEDIUM" in risk:

            st.warning(risk)

        else:

            st.success(risk)



        st.write(
            "### 🚨 Detected Phishing Indicators:"
        )


        if detected:


            for item in detected:

                st.warning(item)


        else:

            st.success(
                "No suspicious keywords detected."
            )



        st.write(
            "### 🔐 Safety Recommendation:"
        )


        if "HIGH" in risk:


            st.error(
                "Do not click links, share OTPs, passwords, or banking details."
            )


        elif "MEDIUM" in risk:


            st.warning(
                "Verify the sender before taking any action."
            )


        else:


            st.success(
                "Message appears safe, but always stay cautious."
            )


    else:


        st.warning(
            "Please enter a message first."
        )
