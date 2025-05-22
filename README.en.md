[中文版 README](./README.md)

# Alert Bot (xAI Live Search Solution)

This project is a creative prototype for an automated real-time alert and posting bot based on the xAI Live Search API. It periodically searches the latest internet content by keywords, uses AI to generate concise summaries, and automatically posts them to X (Twitter). **Note: This project is for creative demonstration only, is unverified, and will not be maintained unless otherwise stated.**

---

## Features
1. **Live Search**: Periodically (default: every 60 seconds) fetches the latest content by keywords.
2. **grok_analyzer**: Analyzes search results and generates concise alert summaries using AI.
3. **x_poster**: Automatically posts the summaries to X (Twitter).

---

## Installation & Usage

### 1. Clone the repository
```bash
git clone <repo_url>
cd <repo_dir>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
Set the following environment variables (via .env file or your system):
- `XAI_API_KEY`: xAI API key
- `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`: X (Twitter) API credentials

### 4. Configure keywords
Edit `config/settings.py` and modify the `KEYWORDS` list to customize the monitored keywords.

### 5. Run the project
```bash
python run.py
```

---

## Project Structure
```
project_root/
│
├── config/
│   ├── __init__.py
│   ├── settings.py         # Keyword and parameter configuration
│   └── logging_config.py   # Logging config (auto-creates logs directory)
│
├── src/
│   ├── __init__.py
│   ├── main.py             # Main workflow
│   ├── data/
│   │   ├── __init__.py
│   │   └── live_search.py  # Real-time search
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── keyword_matcher.py
│   │   └── grok_analyzer.py
│   └── notification/
│       ├── __init__.py
│       └── x_poster.py     # Auto-posting
│
├── requirements.txt
├── run.py                  # Entry point
└── README.md
```

---

## Dependencies
- openai==1.30.0
- tweepy==4.14.0

---

## Logging
Logs are written to `logs/alert_bot.log`. The logs directory is auto-created on first run.

---

## Notes
- Make sure all API keys are set, otherwise the program will exit and log an error.
- You can adjust keywords anytime in `config/settings.py`.
- Requires Python 3.8 or above.

---

## Contact & Support
For custom development, deployment support, or questions, please contact the maintainer:

[SamGor三哥](https://x.com/biggor888) 