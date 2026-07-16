import streamlit as st
from parser import extract_text
from agents import analyze_resume, job_match_analysis

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")

st.caption(
    "Analyze resumes using Gemini AI. Get ATS feedback, skill analysis, career guidance, project suggestions, and optional job matching."
)

st.sidebar.title("📂 Upload Files")

uploaded_resume = st.sidebar.file_uploader(
    "📄 Resume (PDF)",
    type=["pdf"]
)

uploaded_jd = st.sidebar.file_uploader(
    "💼 Job Description (Optional)",
    type=["pdf", "txt"]
)

if uploaded_resume and st.button("🚀 Analyze Resume"):
    resume_text = extract_text(uploaded_resume)
    jd_text = ""

    if uploaded_jd:
        if uploaded_jd.name.lower().endswith(".pdf"):
            jd_text = extract_text(uploaded_jd)
        else:
            jd_text = uploaded_jd.read().decode("utf-8")

    try:
        with st.spinner("Analyzing resume..."):
            result = analyze_resume(resume_text)
            

        st.success("✅ Analysis Complete!")

        resume = result["resume"]
        ats = result["ats"]
        skills = result["skills"]
        career = result["career"]
        projects = result["projects"]

        report = f"""
====================================
        AI RESUME ANALYSIS REPORT
====================================

        Name : {resume.get("name","N/A")}
        Email: {resume.get("email","N/A")}
        Phone: {resume.get("phone","N/A")}

        ATS Score : {ats.get("ats_score","N/A")}%

        Strengths
        ---------
        """

        for item in ats.get("strengths", []):
         report += f"• {item}\n"

         report += "\nAreas for Improvement\n----------------------\n"

        for item in ats.get("weaknesses", []):
         report += f"• {item}\n"

         report += "\nMissing Keywords\n----------------------\n"

        for item in ats.get("missing_keywords", []):
         report += f"• {item}\n"

         report += "\nRecommendations\n----------------------\n"

        for item in ats.get("recommendations", []):
         report += f"• {item}\n"

        

        job_match = None
        if jd_text:
            job_match = job_match_analysis(resume_text, jd_text)

    except Exception as e:
        st.error(str(e))
        st.stop()

    tabs = st.tabs(["📄 Resume","📊 ATS","🧠 Skills","🎯 Career","🚀 Projects","💼 Job Match"])
    tab1,tab2,tab3,tab4,tab5,tab6 = tabs

    with tab1:

     st.subheader("👤 Personal Information")

    st.write(f"**Name:** {resume.get('name','N/A')}")
    st.write(f"**Email:** {resume.get('email','N/A')}")
    st.write(f"**Phone:** {resume.get('phone','N/A')}")

    st.divider()

    st.subheader("🎓 Education")

    for edu in resume.get("education", []):
        st.write(f"**{edu.get('degree', 'N/A')}**")
        st.write(edu.get("institution", "N/A"))
        st.write(f"Graduation: {edu.get('graduation_year', 'N/A')}")
        st.write(f"CGPA: {edu.get('gpa', 'N/A')}")
       
        st.write("")

    st.divider()

    st.subheader("🛠 Skills")

    st.write(", ".join(resume.get("skills", [])))

    st.divider()

    st.subheader("📜 Certifications")

    for cert in resume.get("certifications", []):
        st.write(f"✅ {cert}")

    st.divider()

    st.subheader("🚀 Projects")

    for project in resume.get("projects", []):
        st.markdown(f"### {project['title']}")
        st.write(project["description"])

    with tab2:

     st.subheader("📊 ATS Analysis")

    score = ats.get("ats_score", 0)

    st.metric("ATS Score", f"{score}%")

    if isinstance(score, (int, float)):
        st.progress(score / 100)

    st.divider()

    st.subheader("✅ Strengths")

    for item in ats.get("strengths", []):
        st.success(item)

    st.divider()

    st.subheader("⚠ Areas for Improvement")

    for item in ats.get("weaknesses", []):
        st.warning(item)

    st.divider()

    st.subheader("🔑 Missing Keywords")

    st.write(", ".join(ats.get("missing_keywords", [])))

    st.divider()

    st.subheader("💡 Recommendations")

    for item in ats.get("recommendations", []):
        st.info(item)

    with tab3:
        st.subheader("🧠 Skills Analysis")
        st.json(skills)

    with tab4:
        st.subheader("🎯 Career Recommendations")
        st.json(career)

    with tab5:
        st.subheader("🚀 Suggested Projects")
        st.json(projects)

    with tab6:
        if job_match:
            st.subheader("💼 Job Match Analysis")
            st.json(job_match)
        else:
            st.info("Upload a Job Description to enable this feature.")

    st.divider()

    st.download_button(
    "📄 Download Analysis Report",
    data=report,
    file_name="AI_Resume_Report.txt",
    mime="text/plain"
)

    st.divider()

    st.caption(
    "Built with ❤️ using Python • Streamlit • Google Gemini • PyMuPDF"
)        
