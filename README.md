# 📄 AI Resume Parser & ATS Resume Scorer

An AI-powered Resume Parser and ATS Resume Scorer built using **Python**, **Groq LLM**, and **Pydantic**. The application extracts structured information from PDF/DOCX resumes, compares candidates against a job description, and generates an ATS-style compatibility score with detailed feedback.

---

## 🚀 Features

- 📑 Parse resumes from PDF and DOCX files
- 🤖 Extract structured candidate information using LLMs
- 💼 Analyze job descriptions automatically
- 🎯 Match resumes with job requirements
- 📊 Generate ATS-style compatibility scores
- ✅ Identify matching and missing skills
- 📝 Provide hiring recommendations

---

## 🛠️ Tech Stack

- Python 3.14
- Groq API
- GPT-OSS-120B
- Pydantic
- PyPDF
- python-docx
- python-dotenv
- uv (Python Package Manager)

---

## 📂 Project Structure

```
AI-Resume-Parser/
│
├── Resume_Parser.py      # Main application
├── main.py
├── pyproject.toml
├── uv.lock
├── .gitignore
├── README.md
└── .env.example          # Sample environment variables
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Subhajit05Dutta/AI-Resume-Parser.git
cd AI-Resume-Parser
```

### Install dependencies

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
uv run Resume_Parser.py
```

---

## 📈 Output

For each resume, the system generates:

- Candidate Name
- ATS Match Score
- Matching Skills
- Missing Skills
- Experience Match
- Final Hiring Recommendation

It also ranks the **Top Candidates** and **Lowest Candidates** based on their ATS score.

---

## 📌 Future Improvements

- Streamlit Web Interface
- Resume Ranking Dashboard
- Batch Resume Upload
- Support for More File Formats
- Export Results to CSV/Excel
- Semantic Search with Vector Database
- RAG-based Resume Analysis

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Subhajit Dutta**

- GitHub: https://github.com/Subhajit05Dutta

