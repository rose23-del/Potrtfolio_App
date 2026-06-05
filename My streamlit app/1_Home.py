import streamlit as st

st.set_page_config(
    page_title="My Web App | Home",
    page_icon="🚀",
    layout="wide"
)

with st.sidebar:
    st.title("Navigation")
    st.info("Select a page above to explore.")
    st.divider()
    st.caption("Powered by Streamlit")

col1, col2 = st.columns([2, 1])

with col1:
    st.title("🌐 Welcome to My Web Application")
    st.subheader("Building digital experiences with Python")
    st.write("""
    Hi! I'm glad you're here. This is my personal multipage web application 
    where I showcase my projects and experiments. 
    
    Feel free to look around using the sidebar!
    """)

with col2:
    
    st.image("My streamlit app/pages/FB_IMG_17769307678387414.jpg", width=200)

st.divider()

st.header("✨ What's Inside?")
f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown("### 📊 Interactive")
    st.write("Dynamic charts and data visualization.")

with f_col2:
    st.markdown("### 🛠️ Portfolio")
    st.write("A deep dive into my personal coding projects.")

with f_col3:
    st.markdown("### 📩 Contact")
    st.write("Reach out to me directly through the form.")

st.divider()

st.header("🤝 Let's Connect")
name_input_col, button_col = st.columns([3, 1])

with name_input_col:
    name = st.text_input("What should I call you?", placeholder="Rose R. Delacruz...")

with button_col:
    st.write(" ") # Padding
    st.write(" ") # Padding
    greet_btn = st.button("Say Hello!", use_container_width=True)

if greet_btn:
    if name:
        st.balloons() 
        st.success(f"### Hello,! Nice to meet you! 😊")
    else:
        st.warning("Rose R. DelaCruz.")
