# Career-Advisor-AI-ChatBot 💼

**🚀 Project Overview :**

The AI Career Advisor is a production-ready, cloud-deployed Generative AI application designed to provide structured and actionable career and education guidance. Built using Python, Streamlit, and Google Gemini API, the system delivers intelligent responses including skill recommendations, certifications, learning roadmaps, and step-by-step career plans.

The application follows clean modular architecture with clear separation of concerns across API handling, prompt management, response validation, memory management, and UI layers. It incorporates advanced prompt engineering techniques to ensure structured JSON-based outputs and consistent response quality.

To enhance reliability and responsible AI usage, the system integrates an AI-based guardrail classifier to filter non-career-related queries, implements retry logic for API resilience, and includes token usage tracking for monitoring model consumption and cost optimization. Multi-turn conversation memory enables contextual and interactive user experiences.

The application is deployed on AWS EC2 with secure environment variable management, virtual environment configuration, and public endpoint access, demonstrating end-to-end development from design to cloud deployment.

---

**🧠 Key Features :**

- 🤖 Integration with Google Gemini API for intelligent response generation

- 📄 Structured JSON-based outputs for consistent and reliable career guidance

- 🛡 AI-based guardrail system to filter non-career-related queries

- 🔁 Retry mechanism for improved API reliability and fault tolerance

- 📊 Token usage tracking for monitoring model consumption and cost awareness

- 💬 Multi-turn conversation memory for contextual interactions

- 🖥 Interactive Streamlit chat interface with real-time response rendering

- 🔐 Secure API key management using environment variables

- ☁️ Cloud deployment on AWS EC2 with public endpoint access

---

**🏗 Architecture :**

The project follows a modular and maintainable structure:

career_advisor_app/

```text
│
├── app.py                # Streamlit UI layer
├── gemini_client.py      # Gemini API integration
├── prompt_manager.py     # Prompt engineering logic
├── memory.py             # Multi-turn conversation memory
├── validator.py          # Structured response validation
├── config.py             # Configuration settings
├── utils.py              # Logging utilities
├── requirements.txt      # Project dependencies
└── .env                  # Environment variables (not committed)
```

**🔹 Layered Structure :**

- UI Layer → Streamlit-based frontend interface

- Application Layer → Prompt construction and memory handling

- Infrastructure Layer → Gemini API communication and response processing

- Configuration Layer → Centralized configuration management

This separation improves scalability, maintainability, and testability.

---

**🛠 Tech Stack :**

- Programming Language: Python

- Frontend Framework: Streamlit

- Large Language Model: Google Gemini API

- Cloud Platform: AWS EC2 (Ubuntu)

- Architecture Pattern: Modular Clean Architecture

- Security: Environment-based configuration (.env)

- Logging: Python Logging Module

---

**📦 Installation (Local Setup) :**

**1️⃣ Clone Repository :**

```
git clone https://github.com/msns-1927/Career-Advisor-AI-ChatBot
cd Career-Advisor-AI-ChatBot
```
**2️⃣ Create Virtual Environment :**

```
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```
**3️⃣ Install Dependencies :**

```
pip install -r requirements.txt
```
**4️⃣ Set Environment Variables :**

Create a ``` .env ``` file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```
**5️⃣ Run the Application :**
```
streamlit run app.py
```
---

**☁️ AWS Deployment Steps (Summary) :**

1. Launch an EC2 instance (Ubuntu 22.04 recommended).
2. Configure the security group to allow inbound traffic on Port 8501.
3. Connect to the instance via SSH.
4. Install Python and required dependencies.
5. Upload or clone the project repository.
6. Create a .env file and configure the Gemini API key.
7. Start the application using:
```
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```
8. The application will then be accessible via the instance’s public IP address.

---

**📊 System Capabilities :**

- Generates structured and actionable career guidance
- Supports context-aware multi-turn conversations
- Filters irrelevant queries using AI-based classification
- Validates structured responses before displaying output
- Tracks token usage to optimize model cost and efficiency
- Ensures resilience through retry mechanisms

---

**🔐 Security Practices :**

- No hardcoded credentials within the source code

- API key securely managed using environment variables

- ``` .env ``` file excluded from version control via ``` .gitignore ```

- Session-based memory without persistent storage of user data

---

**🎯 Learning Outcomes :**

- Hands-on experience integrating Generative AI APIs into real-world applications
- Implementation of advanced prompt engineering techniques
- Practical understanding of AI safety through guardrail mechanisms
- Designing modular, maintainable application architecture
- Deploying AI applications to the cloud using AWS EC2
- Monitoring and optimizing token usage for cost control

---

**📌 Future Enhancements :**

- Add model selection options (e.g., Flash / Pro variants)
- Introduce temperature and response configuration controls
- Enable conversation export (PDF or downloadable format)
- Configure Nginx reverse proxy with HTTPS
- Containerize the application using Docker
- Implement CI/CD pipeline for automated deployment

---

**👨‍💻 Author :**

**Siva Narayana Muppidi**
- Aspiring Data Scientist | AI & ML Enthusiast
- LinkedIn: https://www.linkedin.com/in/siva-narayana-muppidi-413259230/
- GitHub: https://github.com/msns-1927

---

**📜 License :**

© 2026 **Siva Narayana Muppidi**. All Rights Reserved.

This project is the intellectual property of the author. The code and content may not be copied, modified, distributed, or used commercially without explicit permission from the author.

---

**⭐ If you found this project useful or interesting, feel free to star the repository!**
