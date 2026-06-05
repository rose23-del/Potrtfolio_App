import streamlit as st

st.set_page_config(page_title="My Skills", page_icon="🛠️", layout="wide")

st.title("🛠️ Technical Skills & Proficiency")
st.write("A summary of my technical toolkit and the level of expertise I've gained through various projects.")

# --- SKILLS LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Programming Languages")
    
    # Python
    st.write("Python")
    st.progress(90)
    
    # SQL
    st.write("SQL")
    st.progress(75)
    
    # Java/C++ (Optional)
    st.write("JavaScript")
    st.progress(60)

with col2:
    st.subheader("Tools & Frameworks")
    
    # Streamlit
    st.write("Streamlit (Web Dev)")
    st.progress(85)
    
    # Git/GitHub
    st.write("Git & Version Control")
    st.progress(80)
    
    # Pandas/Data Analysis
    st.write("Data Analysis (Pandas/NumPy)")
    st.progress(70)

st.markdown("---")

# --- INTERACTIVE SECTION ---
st.subheader("Extra Competencies")

# Using 'tags' or 'pills' for soft skills or minor tools
skills_tags = ["UI/UX Design", "Problem Solving", "Database Management", "API Integration", "Agile Methodology"]
st.write(" ".join([f"{skill}" for skill in skills_tags]))

with st.expander("See My Learning Roadmap"):
    st.write("""
    - *Currently Learning:* Deep Learning and Neural Networks.
    - *Next Goal:* Mastering Cloud Deployment (AWS/Azure).
    - *Certification:* Completed 'Python for Data Science' on Coursera.
    """)