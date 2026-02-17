<h1 align="center">OpenAI Integration API</h1>

<p align="center">

A production-ready FastAPI application that integrates with OpenAI’s Chat Completion API to generate AI-powered responses.  
This project demonstrates asynchronous API handling, secure environment configuration, structured request/response modeling, and robust error management for real-world AI applications.

</p>



##  Overview

This API provides a `/chat` endpoint that accepts a user prompt and returns an AI-generated response using OpenAI's GPT model (`gpt-4o-mini`).  

It is designed for:
- AI-powered chatbots
- Virtual assistants
- Text generation systems
- Workflow automation tools
- Backend AI integrations



## ✨ Features

- Asynchronous communication with OpenAI API using `httpx.AsyncClient`
- Secure API key management via environment variables
- Structured request and response models using Pydantic
- Proper HTTP exception handling
- Production-ready FastAPI architecture
- Auto-generated interactive API documentation


## 🛠 Tech Stack

- **Framework:** FastAPI
- **Server:** Uvicorn
- **HTTP Client:** httpx (async)
- **Data Validation:** Pydantic
- **AI Model:** OpenAI GPT-4o-mini
- **Language:** Python 3.9+



## 🧠 Architecture Highlights

- Fully asynchronous request handling
- Clean separation of request/response models
- Centralized error management
- Environment-based configuration for security
- Easily extendable for:
  - Conversation memory
  - Multiple AI models
  - Rate limiting
  - Authentication
  - Logging & monitoring


##  Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<safashafqaat>/openai-integration-api.git
cd openai-integration-api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / Mac**
```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Set your OpenAI API key as an environment variable:

**Linux / Mac**
```bash
export OPENAI_API_KEY="your_openai_api_key"
```

**Windows (PowerShell)**
```bash
setx OPENAI_API_KEY "your_openai_api_key"
```

Restart your terminal after setting the key.

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```



## 📡 API Endpoint

### POST `/chat`

#### Request Body
```json
{
  "prompt": "Explain artificial intelligence in simple terms."
}
```

#### Response
```json
{
  "prompt": "Explain artificial intelligence in simple terms.",
  "ai_response": "Artificial intelligence is the ability of computers to think and learn like humans..."
}
```



## 📜 License

This project is open-source and available under the MIT License.
