import streamlit as st

st.set_page_config(page_title="My Projects", page_icon="💼", layout="wide")

st.title("💼 My Projects Portfolio")
st.write(".")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2829/2829804.pnG", width=100)
    st.subheader("IoT Smart Irrigation")
    st.info("Category: IoT & Automation")
    st.write(".")
    
    with st.expander("Technical Details"):
        st.write("""
        - *Hardware:* ESP32, Soil Moisture Sensor
        - *Language:* C++, Python
        - *Feature:* Real-time data monitoring.
        """)
    st.link_button("View Code", "Rose935/")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3589/3589030.png", width=100)
    st.subheader("Attendance System")
    st.info("Category: Web Application")
    st.write("Web-based system attendance tracker.")
    
    with st.expander("Technical Details"):
        st.write("""
        - *Backend:* Python (Streamlit)
        - *Database:* SQLite / Google Sheets API
        - *Feature:* Export to Excel function.
        """)
    st.link_button("Demo App", "https://share.streamlit.io/")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/1005/1005141.png", width=100)
    st.subheader("Portfolio Website")
    st.info("Category: Personal Brand")
    st.write("Website streamlit.")
    
    with st.expander("Technical Details"):
        st.write("""
        - *Framework:* Streamlit
        - *Styling:* Custom CSS & Markdown
        - *Feature:* Multipage Navigation.
        """)
    st.link_button("View Repository", "https://github.com/")

st.divider()

st.write("### Good?")
feedback = st.text_area("Tagpu:")
if st.button("Submit Feedback"):
    if feedback:
        st.balloons()
        st.success("Thank you.")
    else:
        st.warning("Good luck.")
