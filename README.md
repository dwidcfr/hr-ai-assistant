# 🧠 AI Resume Matcher

AI Resume Matcher is a Streamlit-based web app that helps HR teams and recruiters:
- ✅ Match candidate resumes with job descriptions
- 📊 Rank multiple candidates by relevance
- ✍️ Generate professional cover letters
- 🛠 Improve resumes using LLMs (like Gemini, LLaMA)

---

## 🚀 Features

- Upload job descriptions (PDF, TXT, DOCX) or write them manually
- Upload multiple candidate resumes
- Get relevance-based ranking of candidates
- Download results in `.txt` and `.docx` formats
- Fully LLM-powered using:
  - 🦙 LLaMA 3 via Groq API
  - 🔷 Gemini via Google Generative Language API

---

## 🛠 Setup

1. Clone the repo

bash
git clone https://github.com/your_username/ai_resume_matcher.git
cd ai_resume_matcher

2. Create .env file from sample
cp .env.sample .env

3. Install dependencies (recommend using virtualenv)
pip install -r requirements.txt

4. Run Streamlit app
streamlit run app.py

