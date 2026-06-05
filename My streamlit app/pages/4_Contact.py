import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📞")

st.title("📞 Get In Touch")
st.write("Have a question or want to work together? Fill out the form below!")

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Rose", placeholder="delacruz")
    with col2:
        email = st.text_input("Email Address", placeholder="delacruzjlrose215@gmail.com")
        
    subject = st.selectbox("Subject", ["General Inquiry", "Project Proposal", "Feedback", "Other"])
    message = st.text_area("Good", placeholder="Good luck...")
    
    submit_button = st.form_submit_button("Hi")

if submit_button:
    if not name or not email or not message:
        st.error("Please fill out all required fields.")
    else:
        st.success(f"Thank you, {name}! Your message regarding '{subject}' has been sent.")
        st.balloons()

with st.sidebar:
    st.header("Alternative Contact")
    st.write("📧 email@yourdomain.com")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("💻 [GitHub](https://github.com/yourusername)")
