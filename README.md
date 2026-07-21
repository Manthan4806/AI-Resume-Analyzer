  AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Streamlit, and Google's Gemini API**. This application analyzes resumes, provides ATS-style feedback, recommends skills and projects, and compares resumes with job descriptions to help users improve their chances of landing interviews.

---

 Features

- 📄 Upload PDF resumes
- 📝 Automatic resume text extraction
- 📊 ATS-style resume analysis
- 💡 Skill gap identification
- 🛠️ Project recommendations
- 🎯 Career improvement suggestions
- 📌 Job Description (JD) matching
- 🌐 Deployed as a live web application

---

 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Model:** Google Gemini 2.5 Flash
- **PDF Processing:** PyMuPDF
- **Environment Management:** python-dotenv
- **Deployment:** Render

---

 Project Structure

```
AI-Resume-Analyzer/
│── app.py
│── agents.py
│── parser.py
│── prompts.py
│── requirements.txt
│── .gitignore
│── knowledge_base/
└── README.md
```

---

 Installation

 1. Clone the repository

```bash
git clone https://github.com/Manthan4806/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

 2. Install dependencies

```bash
pip install -r requirements.txt
```

 3. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

 4. Run the application

```bash
streamlit run app.py
```

---

 Live Demo

  
https://ai-resume-analyzer-60qo.onrender.com

---

 Application Workflow

1. Upload a PDF Resume
2. (Optional) Enter a Job Description
3. Click **Analyze Resume**
4. View:
   - Resume Summary
   - ATS Feedback
   - Skill Recommendations
   - Project Suggestions
   - Career Guidance
   - Job Match Analysis

---

 Challenges Faced

- Handling inconsistent AI-generated responses
- Extracting text from different resume formats
- Managing Gemini API integration
- Resolving deployment and dependency issues

---

 Key Learnings

- Integrated Large Language Models (Gemini) into a real-world application.
- Improved prompt engineering and API integration skills.
- Gained experience in building, debugging, and deploying AI-powered applications.

---

  Author

**Manthan Sanath Rao**

GitHub:  
https://github.com/Manthan4806


 License

This project is developed for educational and portfolio purposes.
