import streamlit as st

def query_support():
    st.header("🗣️ விவசாயி கேள்வி அமைப்பு (Farmer Query Support)")

    query_type = st.radio(
        "உள்ளீட்டின் வகையை தேர்ந்தெடுக்கவும்:",
        ("Text", "Image", "Speech")
    )

    if query_type == "Text":
        question = st.text_area("உங்கள் கேள்வியை தமிழில் அல்லது ஆங்கிலத்தில் எழுதுங்கள்:")
        if st.button("பதில் காண்க"):
            if question.strip():
                # placeholder simple logic — replace with LLM or database lookup
                if "நீர்" in question or "irrigation" in question.lower():
                    st.success("பாசனம்: மழை மற்றும் மண் நிலைக்கு பொருத்தமா பாசன முறைகளை பரிந்துரைக்கவும்.")
                else:
                    st.info("Demo response: உங்கள் கேள்வி பதிவாக்கப்பட்டது. சிறந்த பதில் உடனே வழங்கப்படும்.")
            else:
                st.warning("தயவு செய்து கேள்வியைக் குறிப்பிடவும்.")

    elif query_type == "Image":
        image = st.file_uploader("படத்தை பதிவேற்றவும் (jpg/png)", type=["jpg", "jpeg", "png"])
        if image is not None:
            st.image(image, caption="பதிவேற்றப்பட்ட படம்", use_column_width=True)
            st.info("Image received — image-based diagnosis not yet implemented in demo.")

    elif query_type == "Speech":
        st.info("Speech input not enabled in this demo. Use Text input for now.")
