# Web Watchdog 🐾

A lightweight, modular toolkit for monitoring the health of static websites—especially GitHub Pages setups. Designed to track DNS propagation, SSL validity, and uptime with clarity and minimal fuss.

## 🔧 Features
- 🔍 DNS resolution and propagation checks
- 🔐 SSL certificate expiry and validity
- 🌐 Uptime monitoring via HTTP status codes
- 📬 Optional alerting via email or webhook

## 🚀 Usage
1. Define targets in `config/targets.yaml`
2. Run individual checks from the `monitor/` folder
3. View logs in `logs/monitor.log`

## 🧠 Philosophy
Minimal. Functional. Curious.  
Crafted to reveal what’s working—and what’s quietly failing.

## 📦 Requirements
- Python 3.10+
- `requests`, `dnspython`, `OpenSSL`, `PyYAML`

## 📄 License
MIT
