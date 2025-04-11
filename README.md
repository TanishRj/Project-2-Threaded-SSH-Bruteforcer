# 🧵 Threaded SSH Bruteforcer 🔐

A multi-threaded SSH brute-force tool written in Python, designed for **ethical hacking** and **penetration testing** scenarios. This tool attempts to crack SSH credentials using a given username and a password wordlist — with the power of threading for speed and efficiency.

---

## ✨ Introduction

SSH (Secure Shell) is one of the most used protocols for remote login, making it a **prime target for brute-force attacks**. In this project, we use **Python + Paramiko** and **threading** to create a faster, more scalable brute-force tool.

This tool:
- Accepts a target IP, username, and password file
- Uses threads to attempt multiple logins simultaneously
- Detects and prints successful credentials
- Stops scanning once valid credentials are found

---

## 📌 Features

- ✅ Multi-threaded brute-force attacks
- ✅ Stops after the first successful login
- ✅ Supports custom SSH usernames and password files
- ✅ Clean, color-coded terminal output
- ✅ Detects incorrect paths for wordlists
- ✅ Gracefully handles connection closures

---

## ⚠️ Legal Disclaimer

> This tool is designed for **educational purposes only**.  
> Use it **only on systems you own or have permission to test**.  
> Unauthorized access to systems is **illegal** and **unethical**.

---

## 🛠️ Prerequisites

Install the required Python libraries:

```bash
pip install paramiko termcolor
