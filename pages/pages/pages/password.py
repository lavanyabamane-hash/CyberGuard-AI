import streamlit as st
import re


st.set_page_config(
    page_title="Password Security Analyzer"
)


st.title("🔐 Password Security Analyzer")

st.write(
    "Check your password strength and get security recommendations."
)


password = st.text_input(
    "Enter your password",
    type="password"
)


def check_password(password):

    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("❌ Use at least 8 characters")


    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("❌ Add uppercase letters (A-Z)")


    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("❌ Add lowercase letters (a-z)")


    # Number check
    if re.search(r"[0-9]", password):
        score += 20
    else:
        suggestions.append("❌ Add numbers")


    # Special character check
    if re.search(r"[@$!%*?&#]", password):
        score += 20
    else:
        suggestions.append("❌ Add special characters (@,$,!,%,*)")


    # Strength
    if score >= 80:
        strength = "🟢 Strong"

    elif score >= 50:
        strength = "🟡 Medium"

    else:
        strength = "🔴 Weak"


    return score, strength, suggestions



if password:

    score, strength, suggestions = check_password(password)


    st.write("## 🔐 Analysis Result")


    st.write(
        "Password Strength:",
        strength
    )


    st.progress(score / 100)


    st.write(
        "Security Score:",
        f"{score}/100"
    )


    st.write("### Recommendations")


    if suggestions:

        for item in suggestions:
            st.warning(item)

    else:

        st.success(
            "✅ Your password follows strong security practices!"
        )
