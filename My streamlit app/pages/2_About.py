import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👤")

st.title("👤 About Me")

col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    st.image("My streamlit app/pages/FB_IMG_17769307678387414.jpg", width=200)

with col2:
    st.subheader("How are you! I'm Rose R. Delacruz")
    st.write("""
    I am a student passionate about technology and web development.
    I enjoy building applications, exploring data, and learning new tools.
    """)
    st.info("🚀 Goal: To become a proficient Python Developer.")

st.divider()

st.subheader("🎯 My Expertise")

skill_col1, skill_col2 = st.columns(2)

with skill_col1:
    st.write("*Technical Skills*")
    st.markdown("- ✅ Python\n- ✅ Streamlit\n- ✅ HTML\n- ✅ Networking")

with skill_col2:
    st.write("*Soft Skills*")
    st.markdown("- 🧠 Problem Solving\n- 🤝 Team Collaboration\n- ✍️ Documentation")

st.divider()

st.subheader("📊 Proficiency Level")


st.write("Streamlit: 60%")
st.progress(60)

st.write("Networking: 50%")
st.progress(50)

with st.expander("Adjust my progress (Interactive)"):
    new_level = st.slider("Select level to update", 0, 100)
    st.write(f"Updated skill view: {new_level}%")

st.divider()

st.subheader("📫 Let's Connect")
contact_col1, contact_col2,= st.columns(2)

with contact_col1:
    st.link_button("GitHub", "https://github.com/Rose935")
with contact_col2:
    st.link_button("Gmail", "mailto:your-delacruzjlrose215@gmail.com")



