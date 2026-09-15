# 🧠 AI Playground API

> **Project 01 | AI Backend Engineering**
>
> **A small API with real engineering underneath.** ⚙️🗿

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-Responses%20API-412991?logo=openai&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-19%20passing-success?logo=pytest&logoColor=white)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 The Idea

AI Playground API is a FastAPI backend built to establish the first
foundation of an AI-powered backend system.

Instead of stopping at:

```text
Client → LLM → Response
```

the project introduces the backend engineering around that interaction:

```text
Client
  ↓
FastAPI
  ↓
Validation
  ↓
AI Service
  ↓
OpenAI Responses API
  ↓
Usage + Cost
  ↓
Clean API Response
```

The goal is simple:

> **Make communication with an LLM behave like a proper backend service.**

---

## ✨ What It Can Do

| Capability | Included |
|---|:---:|
| 🤖 LLM generation | ✅ |
| 🧩 Structured AI output | ✅ |
| 🎛️ Reasoning control | ✅ |
| 🔢 Token usage | ✅ |
| 💰 Cost estimation | ✅ |
| 🛡️ Provider error handling | ✅ |
| 📝 Application logging | ✅ |
| 🔐 Environment secrets | ✅ |
| 🧪 Automated testing | ✅ |
| ⚙️ GitHub Actions CI | ✅ |

---

## 🌐 API

### `GET /`

Basic service response.

### `GET /health`

Returns the application's health status and version.

### `POST /generate`

Generates a normal LLM response.

Example request:

```json
{
  "prompt": "Explain dependency injection in FastAPI.",
  "model": "gpt-5.6-luna",
  "reasoning_effort": "low",
  "max_output_tokens": 300
}
```

Example response shape:

```json
{
  "text": "Dependency injection in FastAPI...",
  "model": "gpt-5.6-luna",
  "usage": {
    "input_tokens": 12,
    "output_tokens": 95,
    "total_tokens": 107,
    "reasoning_tokens": 0
  },
  "estimated_cost": 0.000116
}
```

---

## 🧩 Structured Generation

### `POST /generate/structured`

Instead of relying on arbitrary model text, the endpoint returns
data through a Pydantic schema.

```python
class StructuredAIResponse(BaseModel):
    answer: str
    summary: str
```

Example:

```json
{
  "answer": "An API allows software systems to communicate.",
  "summary": "APIs provide structured software communication."
}
```

This creates a predictable boundary between model output and backend data.

---

## 🎛️ Request Controls

The request schema supports:

```text
model
reasoning_effort
max_output_tokens
```

Valid reasoning levels:

```text
none
low
medium
high
xhigh
max
```

Input constraints are enforced before requests reach the provider.

---

## 🛡️ Reliability

External services fail.

This project treats those failures as part of the API design.

```text
Provider Timeout
      ↓
AIServiceTimeoutError
      ↓
504 Gateway Timeout
```

```text
Rate Limit
      ↓
AIServiceRateLimitError
      ↓
429 Too Many Requests
```

```text
Connection / Provider Failure
      ↓
Application Exception
      ↓
502 Bad Gateway
```

Provider-specific exceptions are translated into application-level errors
instead of leaking implementation details to API consumers.

---

## 💰 Usage & Cost

Every normal generation response exposes token usage:

```text
Input Tokens
Output Tokens
Total Tokens
Reasoning Tokens
```

The service also calculates an estimated request cost from input and
output token usage.

Cost calculation is isolated in:

```text
app/utils/cost.py
```

> The returned cost is an estimate, not a billing statement.

---

## 📝 Logging

Important AI service events are logged:

```text
Request
  ↓
Provider call
  ↓
Provider response
  ↓
Usage calculation
  ↓
API response
```

Errors are logged without exposing API credentials.

Logging configuration is centralized in:

```text
app/logging_config.py
```

---

## 🏗️ Architecture

```text
                    ┌───────────────┐
                    │    Client     │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │    FastAPI    │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │   Pydantic    │
                    │  Validation   │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │  AI Service   │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │    OpenAI     │
                    │ Responses API │
                    └───────────────┘
```

The main separation is:

```text
HTTP Layer
    ↓
Service Layer
    ↓
Provider Layer
```

This keeps API routing separate from AI-provider communication.

---

## 📁 Project Structure

```text
AI-Playground-API/
│
├── app/
│   ├── exceptions/
│   │   ├── custom_exceptions.py
│   │   └── handlers.py
│   │
│   ├── services/
│   │   └── ai_services.py
│   │
│   ├── utils/
│   │   └── cost.py
│   │
│   ├── config.py
│   ├── logging_config.py
│   ├── main.py
│   └── schemas.py
│
├── tests/
│   ├── test_ai_service_errors.py
│   ├── test_ai_service_request.py
│   ├── test_ai_structured_response_errors.py
│   ├── test_cost.py
│   ├── test_exception_handlers.py
│   ├── test_generate.py
│   ├── test_structured_response.py
│   └── test_validation.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .env.example
├── .gitignore
├── LICENSE
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## 🔐 Configuration

Create a local `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

The real `.env` file is excluded from version control.

A safe template is provided:

```text
.env.example
```

Never commit real API credentials.

---

## 🧪 Testing

Run the complete local test suite:

```bash
python -m pytest -q
```

Current result:

```text
19 passed
```

The real provider test is explicitly marked:

```python
@pytest.mark.integration
```

Run without external provider access:

```bash
python -m pytest -q -m "not integration"
```

Current CI result:

```text
18 passed
1 deselected
```

Run the integration test separately when a valid local API key is available:

```bash
python -m pytest -q -m integration
```

---

## ⚙️ Continuous Integration

GitHub Actions runs automatically on:

```text
push
pull_request
```

Pipeline:

```text
Checkout
   ↓
Python Setup
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
✅ Pass
```

External integration tests are excluded from CI.

CI uses a non-secret placeholder:

```text
OPENAI_API_KEY=ci-test-placeholder
```

No real provider credential is stored in the workflow.

---

## 🚀 Run Locally

### 1. Create environment

```bash
python -m venv .venv
```

### 2. Activate

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure `.env`

```env
OPENAI_API_KEY=your_api_key_here
```

### 5. Start the API

```bash
python -m fastapi dev app/main.py
```

Then explore the generated FastAPI documentation.

---

## 🧠 Engineering Decisions

**Service layer:** keeps provider communication out of route handlers.

**Custom exceptions:** creates a stable application-level error boundary.

**Structured output:** turns model output into validated application data.

**No database:** this project has no persistence requirement.

**No Docker:** containerization is intentionally deferred because this
single-service project has no infrastructure need for it yet.

**Synchronous provider client:** deeper async provider integration is
reserved for workloads where concurrency and streaming actually matter.

---

## 🎯 Scope

This project intentionally does not include:

```text
Database
Authentication
Streaming
Redis
File Processing
Embeddings
Vector Search
RAG
Agents
Tool Calling
Production Deployment
```

Nothing here is accidentally missing.

The project solves its current problem without adding infrastructure
for problems it does not have yet.

---

## 🏁 Status

```text
Core API              ✅
LLM Integration       ✅
Structured Output     ✅
Validation            ✅
Error Handling        ✅
Logging               ✅
Usage Tracking        ✅
Cost Estimation       ✅
Testing               ✅
CI                    ✅
Secret Protection     ✅
Documentation         ✅
License               ✅
```

### 🟢 Project 01 Complete

The playground started with one simple question:

> **Can an LLM become a reliable backend dependency instead of just an API call?**

This project answers that question with a working, tested, documented
service and a clean foundation for everything built on top of it.

**Project 01 shipped. ⚙️🧠🗿**
