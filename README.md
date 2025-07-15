# Gemma Chatbot — Private, Offline AI with a Beautiful UI

A full-stack, privacy-focused chatbot powered by [`gemma:2b`](https://ollama.com/library/gemma) via [Ollama](https://ollama.com/), featuring a Flask API backend and a polished, modern web interface. This project is designed for developers who want local inference, elegant UI/UX, and full control — without relying on OpenAI or internet APIs.

---

## Project Overview

This chatbot showcases how to build an offline-capable, UI-rich AI assistant that:

- Runs entirely **locally on your machine**
- Requires **no API keys**, **no internet**, and **no vendor lock-in**
- Combines the power of open-weight LLMs with modern UI design
- Uses only **Flask** and **Vanilla JavaScript** — no frontend frameworks

Whether you're a student learning LLM integration, a researcher testing model behaviors, or a dev building private AI tools — this template gives you a head start.

---

## Key Features

###  LLM + Backend
- `gemma:2b` model via Ollama — small, capable, open
- Flask API to send prompt → get response from Ollama
- Designed for simplicity and clarity in backend logic

### Frontend Experience
- Fully responsive UI — mobile + desktop
- Stylish **chat bubbles** with **avatars**
- Real-time **timestamps** for every message
- Supports `Enter` to send, `Shift+Enter` for newline
- Auto-focuses input when you open the page
- Theme switcher:  Dark mode /  Light mode toggle
- **Chat history persistence** with `localStorage`

### Local-First
- 100% offline (no cloud connection required)
- You own the data — suitable for private, secure use cases

---

## Tech Stack

| Layer     | Tech Used                  |
|-----------|----------------------------|
| LLM       | [`gemma:2b`](https://ollama.com/library/gemma) via Ollama |
| Backend   | Python 3.9+, Flask, Flask-CORS |
| Frontend  | HTML5, CSS3, Vanilla JS    |
| Model Host| Ollama (locally installed) |

---

## Getting Started

### 1. Prerequisites

- [Install Python 3.9+](https://www.python.org/downloads/)
- [Install Ollama](https://ollama.com/download) and verify with `ollama --version`

### 2. Clone the Repository

```bash
git clone https://github.com/Sourav-x-3202/chatbot.git
cd chatbot
````

### 3. Start the Ollama Model

```bash
ollama run gemma:2b
```

> This will download the model the first time (\~2GB), and serve it at `http://localhost:11434`

Keep this terminal open.

### 4. Run the Flask API

```bash
pip install flask flask-cors requests
python chatbot.py
```

> Flask will run on `http://127.0.0.1:5000`
---

## Screenshots
<img width="1365" height="718" alt="Screenshot 2025-07-15 121845" src="https://github.com/user-attachments/assets/c4f0d830-1ff9-4280-8a6e-bd057d629028" />


### 5. Open the Frontend

Just double-click `chat.html` (or drag it into your browser).
You're now chatting with an offline AI assistant!

---

## Screenshots
<img width="467" height="598" alt="Screenshot 2025-07-15 121714" src="https://github.com/user-attachments/assets/1754a3c2-b889-4cc3-baa9-23299ccbadfe" />


---

##  File Structure

```
chatbot/
├── chatbot.py        # Flask backend
├── chat.html         # Frontend HTML
├── chat.css          # Styling (Dark/Light theme)
├── README.md         # You're reading it
└── .gitignore        # Recommended for Python projects
```

---

##  Recommended Improvements (Advanced Ideas)

*  Streaming token-by-token response display
*  Conversation summarization / memory
*  Voice input and TTS response
*  Export chat to file / PDF
*  Package as a desktop app (Electron + Flask)
*  Host frontend via GitHub Pages

---

## Contributing

Pull requests and ideas are welcome!
Please feel free to fork the repo, open issues, or submit enhancements.

> This project is intentionally framework-free to be educational, clean, and hackable.

---

## Author

**Sourav Sharma**
Developer. Maker. Privacy-first AI enthusiast.
Find me on GitHub → [@Sourav-x-3202](https://github.com/Sourav-x-3202)

---


## Star This Project

If you found this useful, helpful, or inspiring — please consider starring the repository.
It helps others discover the project and keeps development going 

---

