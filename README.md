# 🚀 Flask AI DevOps Starter

A production-ready Flask boilerplate with AI integration (Claude/Anthropic), Docker, and a full CI/CD pipeline via GitHub Actions. Deploy any AI-powered backend in minutes.

> Built by [Your Name] · [Your Gumroad Link]

---

## ✨ What's Included

| Feature | Details |
|---|---|
| **Flask App** | Modular blueprint structure, ready to extend |
| **AI Integration** | Claude (Anthropic) API wired up and ready |
| **Docker** | Multi-stage Dockerfile + docker-compose |
| **CI/CD** | GitHub Actions: test → build → deploy |
| **Tests** | Pytest setup with sample test cases |
| **Security** | Non-root Docker user, env var secrets |

---

## 📁 Project Structure

```
flask-ai-devops-starter/
├── app/
│   ├── __init__.py       # App factory
│   ├── routes.py         # API endpoints
│   └── ai.py             # AI integration (Claude)
├── tests/
│   └── test_routes.py    # Pytest tests
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions pipeline
├── Dockerfile            # Multi-stage Docker build
├── docker-compose.yml    # Local + production compose
├── requirements.txt
├── run.py                # App entry point
└── .env.example          # Environment variable template
```

---

## ⚡ Quick Start

### 1. Clone & install

```bash
git clone https://github.com/YOUR_USERNAME/flask-ai-devops-starter.git
cd flask-ai-devops-starter
pip install -r requirements.txt
```

### 2. Set up environment

```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 3. Run locally

```bash
python run.py
```

### 4. Run with Docker

```bash
docker-compose up --build
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Status check |
| GET | `/health` | Health check (used by Docker) |
| POST | `/ai/ask` | Send a prompt to Claude AI |

### Example: AI Request

```bash
curl -X POST http://localhost:5000/ai/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain DevOps in one sentence"}'
```

**Response:**
```json
{
  "response": "DevOps is the practice of combining development and operations..."
}
```

---

## 🔁 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci-cd.yml`) runs automatically on every push to `main`:

```
Push to main
    │
    ├── ✅ Run pytest tests
    │
    ├── 🐳 Build & push Docker image to Docker Hub
    │
    └── 🚀 SSH into server and deploy with docker-compose
```

### Required GitHub Secrets

Go to **Settings → Secrets → Actions** and add:

| Secret | Value |
|---|---|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Your Docker Hub password |
| `SSH_HOST` | Your server IP address |
| `SSH_USER` | SSH username (e.g. `ubuntu`) |
| `SSH_PRIVATE_KEY` | Your private SSH key |

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🛠 Extending This Template

- **Add a database**: Plug in SQLAlchemy + PostgreSQL in `app/__init__.py`
- **Add auth**: Use Flask-JWT-Extended for token auth
- **Swap AI provider**: Replace `app/ai.py` with OpenAI SDK — same interface
- **Add rate limiting**: Use Flask-Limiter on `/ai/ask`

---

## 📄 License

MIT — free to use for personal and commercial projects.

---

## 🙋 Support

If you bought this template and need help, reach out at: **your@email.com**
