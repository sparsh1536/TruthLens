# 🛡️ TruthLens

> **Question Claims. Verify Facts.**

TruthLens is an AI-powered fact-checking system that analyzes YouTube videos by extracting factual claims, retrieving relevant online evidence, and evaluating whether the available evidence supports those claims.

---

## ✨ Features

* 🎥 Analyze YouTube videos from a URL
* 🎙️ Automatic speech transcription using Faster Whisper
* 🧠 AI-powered claim extraction and classification
* 🌐 Web evidence retrieval using Tavily Search
* 🤖 Claim verification using a local Gemma 3 model via Ollama
* 📊 Confidence-based verification reports
* 🔒 Runs locally for privacy

---

## 🏗️ How It Works

```text
YouTube URL
     │
     ▼
Download Audio (yt-dlp)
     │
     ▼
Speech-to-Text (Faster Whisper)
     │
     ▼
Claim Extraction (Gemma 3)
     │
     ▼
Claim Classification
     │
     ▼
Web Search (Tavily)
     │
     ▼
Evidence Collection
     │
     ▼
Verification (Gemma 3)
     │
     ▼
Fact-Checking Report
```

---

## 🛠️ Tech Stack

* Python
* Ollama
* Gemma 3
* Faster Whisper
* Tavily Search API
* yt-dlp

---

## 📂 Project Structure

```
TruthLens/
├── backend/
│   ├── downloader.py
│   ├── transcriber.py
│   ├── claim_extractor.py
│   ├── search.py
│   ├── verifier.py
│   ├── pipeline.py
│   └── main.py
├── data/
├── README.md
├── requirements.txt
└── .env.example
```

---

## 🚀 Installation

```bash
git clone https://github.com/sparsh1536/TruthLens.git

cd TruthLens

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
TAVILY_API_KEY=your_api_key_here
```

Run:

```bash
python backend/main.py
```

---

## 📸 Demo

### 1. 🎥 Input Video

![Step 1](docs/screenshots/1.png)

---

### 2. ⬇️ Audio Download

![Step 2](docs/screenshots/2.png)

![Step 3](docs/screenshots/3.png)

---

### 3. 🧠 Claim Extraction, 🌐 Evidence Collection & 🤖 AI Verification

![Step 4](docs/screenshots/4.png)

![Step 5](docs/screenshots/5.png)

---

![Step 6](docs/screenshots/6.png)

![Step 7](docs/screenshots/7.png)

---

![Step 8](docs/screenshots/8.png)

![Step 9](docs/screenshots/9.png)

---

![Step 10](docs/screenshots/10.png)

![Step 11](docs/screenshots/11.png)

---

## 📌 Roadmap

* [x] YouTube audio extraction
* [x] Speech transcription
* [x] Claim extraction
* [x] Web evidence retrieval
* [x] AI verification
* [ ] Web interface
* [ ] Parallel verification
* [ ] Multi-language support
* [ ] PDF & News article fact-checking

---

## 👨‍💻 Author

**Sparsh Soni**

GitHub: https://github.com/sparsh1536

---