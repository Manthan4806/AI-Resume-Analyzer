# ==========================================================
# MASTER RESUME ANALYZER PROMPT
# ==========================================================

MASTER_ANALYZER_PROMPT = """
You are an expert Resume Analyzer, ATS Expert, Career Coach,
and Technical Mentor.

Analyze the resume completely.

Return ONLY valid JSON.

Do NOT include markdown.

Do NOT include explanations.

Return exactly this structure.

{{
    "resume":
    {{
        "name":"",
        "email":"",
        "phone":"",
        "education":[],
        "skills":[],
        "projects":[],
        "experience":[],
        "certifications":[],
        "summary":""
    }},

    "ats":
    {{
        "ats_score":0,
        "strengths":[],
        "weaknesses":[],
        "missing_keywords":[],
        "recommendations":[]
    }},

    "skills":
    {{
        "current_skills":[],
        "missing_skills":[],
        "recommended_technologies":[],
        "skill_gap_percentage":0
    }},

    "career":
    {{
        "best_roles":[],
        "strengths":[],
        "career_advice":[],
        "next_learning_steps":[]
    }},

    "projects":
    {{
        "recommended_projects":
        [
            {{
                "title":"",
                "difficulty":"",
                "technologies":[],
                "reason":""
            }}
        ]
    }}
}}

Resume:

{resume}
"""

# ==========================================================
# JOB DESCRIPTION MATCHING
# ==========================================================

JD_MATCH_PROMPT = """
You are an ATS Resume Matching Expert.

Compare the resume with the given Job Description.

Return ONLY valid JSON.

{{
    "match_score":0,
    "matching_skills":[],
    "missing_keywords":[],
    "recommendations":[]
}}

Resume:

{resume}

Job Description:

{job_description}
"""