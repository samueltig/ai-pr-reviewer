<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" />
</div>

<h1 align="center">🤖 Automated AI Code Reviewer</h1>

<p align="center">
  An intelligent CI/CD pipeline tool that automatically reviews GitHub Pull Requests using OpenAI's GPT-4.
</p>

---

### 📖 About The Project

Code reviews are essential but time-consuming. This project automates the first line of defense in the code review process. By utilizing **GitHub Actions** and the **OpenAI API**, this tool listens for new Pull Requests, fetches the code diffs, analyzes the logic for bugs, security flaws, and performance issues, and posts a professional review directly as a PR comment.

**Key Features:**
- ⚡ **Automated Triggering:** Runs instantly when a PR is opened or updated.
- 🧠 **Context-Aware Analysis:** Uses GPT-4 to understand complex code changes.
- 🛡️ **Secure:** Uses environment variables and GitHub Secrets so API keys are never exposed.
- 🏗️ **Clean Architecture:** Built with Object-Oriented Python, Type Hinting, and logging.

---

### 📂 Repository Structure

```text
ai-pr-reviewer/
├── .github/workflows/
│   └── ai-review.yml       # CI/CD Pipeline Configuration
├── src/
│   ├── ai_agent.py         # OpenAI API Handler
│   ├── github_manager.py   # PyGitHub API Handler
│   └── main.py             # Execution & Logging logic
├── requirements.txt        # Python Dependencies
└── README.md
