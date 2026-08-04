import streamlit as st
from utils.image_analysis import analyze_image


st.set_page_config(
    page_title="Image Analysis"
)


st.title("🖼️ AI Image Analysis")

st.write("Upload a cybersecurity-related image for AI analysis.")


uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        width="stretch"
    )


    if st.button("🔍 Analyze Image"):

        with st.spinner("Analyzing image..."):

            result = analyze_image(uploaded_file)


        st.success("Analysis Completed!")


        st.write("## 🛡️ CyberGuard Analysis")


        # Status
        st.write(
            "### Status:"
        )

        st.info(result["status"])


        # Risk Level
        st.write(
            "### Risk Level:"
        )

        if result["risk"] == "HIGH":
            st.error("🔴 HIGH RISK")

        else:
            st.success("🟢 LOW RISK")


        # Keywords
        st.write(
            "### Detected Keywords:"
        )

        if result["keywords"]:

            for word in result["keywords"]:
                st.warning(word)

        else:

            st.write("No suspicious keywords detected.")


        # OCR Text
        st.write(
            "### Extracted Text:"
        )

        if result["text"].strip():

            st.text(result["text"])

        else:

            st.write("No text detected from image.")
