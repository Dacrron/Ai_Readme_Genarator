# AI-Powered README Generator

## Description

**AI-Powered README Generator** is a web application that automates the creation of professional, comprehensive README files for code repositories. By leveraging large language models (LLMs) such as OpenAI, Gemini, and Perplexity, the platform analyzes codebases, summarizes their structure and features, and generates detailed documentation with minimal manual input. This streamlines the documentation process for developers, ensuring high-quality, standardized project READMEs.

## Architecture

- **FastAPI Backend:** Modular and extensible, responsible for cloning repositories, managing API keys, orchestrating LLM-based summarization, and generating README content.
- **LangChain Map-Reduce Workflow:** Efficiently summarizes large codebases, handling files that exceed LLM context limits.
- **Frontend/UI:** Modern, interactive web interface with real-time feedback, section-based editing, and robust error handling. Built with best-practice CSS for accessibility and maintainability.
- **Security Layer:** Input validation, content sanitization, and secure API key management via environment variables.

## Prerequisites

- **Python 3.9+**
- **Git** (for repository cloning)
- **API Keys** for supported LLM providers (OpenAI, Gemini, Perplexity)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/ai-readme-generator.git
   cd ai-readme-generator
   ```

2. **Backend Setup:**
    Enter into your environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

**Before start** - Make a 'env' folder and set your api key.

1. **Start the project:**
   ```bash
   fastapi run fastapi_app.py
   ```
   This will host the website, most cases it will be        localhost:8000


2. **Generate a README:**
   - Submit a repository URL or upload code via the web interface.
   - Select the desired generation method (currently, only the standard method is available).
   - Preview, copy, or download the generated README.
   - Waiting progress is not shown as it only shows generating so please wait.



## Frontend 
    - Generated with the help of Claude and GPT
    - Only HTML, CSS, and JS for data


    
## Screenshots

![App Screenshot](https://github.com/Dacrron/Ai_Readme_Genarator/blob/main/static/2.png)
![App Screenshot](https://github.com/Dacrron/Ai_Readme_Genarator/blob/main/static/1.png)


