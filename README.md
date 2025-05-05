### ⚙️ CyberUtils

**CyberUtils** is a Python-based CLI tool that provides essential utilities for cybersecurity students, enthusiasts, and professionals. It includes tools for password generation, cybersecurity news aggregation, CVE lookups, and AES encryption demonstrations using various modes.

---

## 🔧 Features

### 1. 🔐 Password Generator
Generate strong, random passwords using letters and digits.
- Input: Desired password length
- Output: Secure password string

### 2. 📰 Cybersecurity News Aggregator
Stay updated with the latest news from top cybersecurity blogs:
- NIST
- The Hacker News
- ThreatPost
- Naked Security
- SecurityWeek
- Google Security Blog

You can select a source, view headlines, and open articles in your browser.

### 3. 🛡️ CVE Search Tool
Search for any CVE by ID and get:
- CVE ID
- Summary / Description

Powered by the [CIRCL CVE API](https://cve.circl.lu/).

### 4. 🧠 CryptoBot – AES Encryption Demo
Explore AES encryption using the following modes:
- ECB (Electronic Codebook)
- CBC (Cipher Block Chaining)
- CFB (Cipher Feedback)
- OFB (Output Feedback)
- CTR (Counter)

Input plaintext and view real-time encryption using randomly generated keys and IVs.

---

## 🧑‍💻 Requirements

- Python 3.x  
- Dependencies (install via pip):

```bash
pip install pyfiglet feedparser requests pycryptodome
```

---

## 🚀 How to Run

```bash
python cyberutils.py
```

You'll be presented with a CLI menu to choose any of the tools.

---

## 📦 Project Structure

```
cyberutils.py       # Main CLI application
```

---

## 📜 License

This project is open-source and licensed under the MIT License.

---

## 🙌 Contributions

Feel free to fork the repo and submit PRs for:
- Bug fixes
- New features (e.g., hashing tools, vulnerability scanners)
- UI/UX improvements for terminal flow

---

## 💬 Author

Built by [Pradyumn Khanchandani](https://www.linkedin.com/in/pradyumn-khanchandani/)

---

**CyberUtils** — The Swiss Army Knife for Cybersecurity Basics 🔐
