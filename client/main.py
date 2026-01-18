import streamlit as st
st.title("Skyreels-V2 Magic Access")
st.write("Powered by Skyreels-V2")
st.title("Step 1: Run this compute engine")
st.info("Background Task: Run this Google Colab")
st.markdown("<center><a target=\"_blank\" href=\"https://colab.research.google.com/drive/1Wq-Gotfckkhkj1S0Y1oqDPit6CnxI3cD?usp=sharing\">"
  "<img height=25 src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Click toOpen In Colab Notebook\"/>"
"</a></center>", unsafe_allow_html=True)
st.title("Step 2: Enter your prompt")
input_text = st.text_area("Enter your prompt here", height=200)
if st.button("Generate Video"):
    with st.spinner("Generating Video..."):
        st.video("https://youtu.be/vw2Yc4Y1PsU?si=grWSZSjDV0X05WN3")


