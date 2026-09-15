# 🧠 AI Playground API

> **Project 01 | AI Backend Engineering**
> **Talk to an LLM. Structure the output. Measure the cost. Handle failure.** ⚙️🗿

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-Responses%20API-412991?logo=openai&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-19%20passing-success?logo=pytest&logoColor=white)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

## 🚀 What It Does

A clean FastAPI backend for experimenting with LLM-powered functionality through the OpenAI Responses API.

```text
Client → FastAPI → Validation → AI Service → OpenAI
                         ↓
                  Usage + Cost
                         ↓
                    Clean Response
```

### ✨ Features

- 🤖 Normal LLM generation
- 🧩 Structured Pydantic AI output
- 🎛️ Model, reasoning & token controls
- 🔢 Token usage tracking
- 💰 Estimated request cost
- 🛡️ Timeout, rate-limit & provider error handling
- 📝 Application logging
- 🔐 Environment-based secret protection
- 🧪 Automated tests + integration-test isolation
- ⚙️ GitHub Actions CI

## 🌐 Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | Service status |
| `GET` | `/health` | Health check |
| `POST` | `/generate` | AI generation |
| `POST` | `/generate/structured` | Structured output |

## 🧪 Test

```bash
python -m pytest -q
```

**19 passed** ✅

CI runs without external provider tests:

```bash
python -m pytest -q -m "not integration"
```

**18 passed, 1 deselected** ✅

## 🛠️ Run

```bash
python -m pip install -r requirements.txt
```

Create `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

Start:

```bash
python -m fastapi dev app/main.py
```

> **Scope matters:** no database, RAG, agents, streaming, or Docker yet.
> This project solves the problem it was designed to solve. 🎯