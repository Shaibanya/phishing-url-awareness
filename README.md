# 🛡️ Phishing URL Awareness Checker

An educational cybersecurity project that helps users identify common warning signs in potentially suspicious URLs. Built with Python, this project includes a command-line checker and a Flask-based web application with a simple, user-friendly interface.

🔗 **Live Demo:** https://phishing-url-awareness.onrender.com/

📂 **GitHub Repository:** https://github.com/Shaibanya/phishing-url-awareness

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Run the Command-Line Checker](#-run-the-command-line-checker)
- [Run the Web Application](#-run-the-web-application)
- [Example](#-example)
- [Testing](#-testing)
- [Screenshots](#-screenshots)
- [Live Demo](#-live-demo)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Ethical Use](#-ethical-use)
- [Author](#-author)
- [Disclaimer](#-disclaimer)

---

## 📖 About the Project

Phishing is a cybersecurity threat in which attackers use deceptive messages and websites to trick people into revealing sensitive information, such as passwords, financial details, or personal data.

Suspicious URLs can sometimes contain warning signs that users can learn to recognize.

The **Phishing URL Awareness Checker** analyzes the text of a URL and identifies selected patterns that may deserve further investigation. It provides explanations to help users understand why a pattern could be suspicious.

The project offers two ways to use the checker:

1. **Command-Line Interface (CLI):** Inspect a URL directly through the terminal.
2. **Web Application:** Enter a URL in a browser and view the detected warning signs.

The application examines URL text without visiting the destination website or making network requests.

### Project Objectives

- Improve awareness of common suspicious URL patterns.
- Demonstrate basic cybersecurity concepts using Python.
- Provide explanations alongside detected warning signs.
- Build a simple web interface using Flask.
- Practice software development, testing, documentation, and deployment.

---

## ✨ Features

- **At-Sign Detection:** Flags URLs containing the `@` symbol.
- **URL Length Check:** Flags URLs longer than 100 characters.
- **IP-Address Detection:** Identifies IPv4-style hostnames.
- **Hostname Label Check:** Flags hostnames containing five or more labels.
- **Punycode Detection:** Detects the `xn--` marker in a hostname.
- **HTTP Detection:** Identifies URLs using the HTTP scheme.
- **Explanatory Results:** Provides a reason for each detected warning.
- **CLI Support:** Allows URL inspection through the terminal.
- **Web Interface:** Provides a browser-based URL checking experience.
- **Malformed Input Handling:** Handles malformed URL input without crashing.
- **Privacy-Conscious Inspection:** Does not visit submitted URLs or make network requests.
- **Responsive Layout:** Uses a simple layout suitable for common desktop and mobile browsers.

> **Important:** These rules identify potential warning signs, not confirmed phishing attacks. A URL with no warnings may still be malicious.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core URL inspection logic |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | Web page styling |
| Git | Version control |
| GitHub | Source code hosting |
| Gunicorn | WSGI server for deployment |
| Render | Web application hosting |

---

## ⚙️ How It Works

The checker applies a set of predefined rules to the URL text supplied by the user.

The current checks include:

1. Checking whether the URL contains `@`.
2. Checking whether the URL exceeds 100 characters.
3. Checking for an IPv4-style hostname.
4. Counting hostname labels and flagging hostnames with five or more labels.
5. Checking for the `xn--` punycode marker.
6. Checking whether the URL uses HTTP.

When a warning is detected, the application displays its explanation.

The checker does not crawl the destination website, download web content, or verify a domain's reputation.

---

## 📁 Project Structure

```text
phishing-url-awareness/
│
├── app.py
├── phishing_checker.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── sample_run.png
│   └── test_results.png
│
└── tests/
    └── test_samples.md
```

### File Descriptions

- `app.py` — Flask web application and browser interface.
- `phishing_checker.py` — Core URL inspection logic and command-line checker.
- `requirements.txt` — Python package dependencies.
- `README.md` — Project documentation.
- `screenshots/` — Project screenshots.
- `tests/test_samples.md` — Documented test cases and results.

---

## 📋 Requirements

Before running the project locally, make sure you have:

- Python 3 installed.
- pip available.
- A web browser for the web interface.
- Git installed if you want to clone the repository.

The deployed web application can be accessed through the live demo link without installing Python locally.

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shaibanya/phishing-url-awareness.git
```

### Step 2: Open the Project Directory

```bash
cd phishing-url-awareness
```

### Step 3: Create a Virtual Environment (Recommended)

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The project is now ready to run locally.

---

## 💻 Run the Command-Line Checker

To start the command-line version, run:

```bash
python phishing_checker.py
```

Follow the prompts to enter a URL.

The checker will inspect the supplied text and display the warning signs identified by its rules.

---

## 🌐 Run the Web Application

The project also includes a Flask-based web interface.

### Step 1: Start the Application

```bash
python app.py
```

### Step 2: Open the Local Website

Open this address in your browser:

http://127.0.0.1:5000/

### Step 3: Enter a URL

Type a URL into the input field and click **Check URL**.

### Step 4: Review the Results

The application displays the detected warning signs and their explanations.

Keep the terminal open while testing the local application. Press `Ctrl + C` in the terminal to stop the development server.

---

## 🧪 Example

### Input

```text
http://192.0.2.10/account
```

### Expected Warning Signs

**1. Uses an IP address instead of a familiar domain.**

An IP-address hostname may deserve extra scrutiny because it does not use a conventional domain name.

**2. Uses HTTP. HTTPS alone does not prove trust.**

HTTP does not provide the transport encryption normally provided by HTTPS. However, HTTPS itself does not guarantee that a website is trustworthy.

The checker displays explanations for the warning signs it detects.

The example IP address is reserved for documentation and is included only for demonstration.

---

## ✅ Testing

The project has been checked against representative URL patterns.

| Test Case | Expected Result |
|---|---|
| Ordinary HTTPS URL | No listed warning signs for the example |
| URL containing an IPv4 address | IP-address warning |
| URL containing `@` | At-sign warning |
| URL with five or more hostname labels | Hostname-label warning |
| URL containing `xn--` | Punycode warning |
| Malformed URL such as `http://[bad` | Error message instead of a crash |

Detailed test cases and recorded results are documented in `tests/test_samples.md`.

These cases cover selected detection rules and malformed input handling. They do not establish whether a URL is genuinely safe or malicious.

---

## 📸 Screenshots

### 1. Command-Line Sample Run

This screenshot demonstrates the command-line checker inspecting a URL.

![Command-line sample run](screenshots/sample_run.png)

### 2. Test Results

This screenshot demonstrates the recorded test results for the project.

![Test results](screenshots/test_results.png)

---

## 🔗 Live Demo

**Try the application online:**

### [Open Phishing URL Awareness Checker](https://phishing-url-awareness.onrender.com/)

The deployed application allows users to enter URL text and review detected warning signs with explanations.

The application is designed for educational awareness and does not visit submitted URLs.

If the hosted service is temporarily starting up, wait a little and refresh the page.

---

## ⚠️ Limitations

This project uses a limited set of heuristic rules and has important limitations:

- It does not guarantee the detection of phishing URLs.
- Legitimate URLs may trigger warnings.
- Malicious URLs may not trigger any warnings.
- It does not visit or inspect destination websites.
- It does not check domain registration information or reputation.
- It does not validate website ownership or trustworthiness.
- It does not establish whether a website's certificate or behavior is safe.
- HTTPS does not guarantee that a website is legitimate.
- A URL with no detected warnings should not automatically be considered safe.

The results should be treated as educational indicators rather than a definitive security assessment.

---

## 🔮 Future Improvements

Possible improvements include:

1. Adding more URL inspection rules.
2. Improving hostname parsing and URL normalization.
3. Adding automated unit tests for individual detection rules.
4. Improving accessibility and mobile usability.
5. Adding clearer validation messages for malformed input.
6. Expanding educational explanations about phishing techniques.
7. Improving the display of results through clearer warning categories.
8. Adding optional integration with reputable URL reputation services, with appropriate privacy and security safeguards.

These are potential future improvements and are not necessarily implemented in the current version.

---

## 🔐 Ethical Use

This project is intended for cybersecurity education, awareness, and demonstration purposes.

Users should:

- Verify website addresses independently before entering sensitive information.
- Avoid sharing passwords, payment details, or confidential information with untrusted websites.
- Understand that a warning does not prove malicious intent.
- Understand that the absence of a warning does not prove safety.

Use the checker as an educational aid alongside careful browsing practices and appropriate security tools.

---

## 👨‍💻 Author

**Shaibanya Dey**

- **GitHub:** https://github.com/Shaibanya
- **Project Repository:** https://github.com/Shaibanya/phishing-url-awareness
- **Live Demo:** https://phishing-url-awareness.onrender.com/

---

## 📜 Disclaimer

This project is provided for educational and cybersecurity awareness purposes only. It does not guarantee the detection of phishing attacks and should not replace professional security tools, independent verification, or careful online browsing practices.

The author is not responsible for decisions made solely on the basis of this tool's results.