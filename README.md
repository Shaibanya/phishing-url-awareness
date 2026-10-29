# EWB Phishing URL Awareness Checker

## Overview

Phishing is a type of online fraud in which attackers use fake links or messages to trick people into sharing sensitive information, such as passwords, OTPs, or payment details.

The Phishing URL Awareness Checker is a beginner-friendly Python project that examines URL text for common phishing warning signs. It helps users recognize potentially suspicious URL patterns without opening websites or sending information anywhere.

This is an educational project designed to improve awareness of online safety.

## Features

The program checks for six warning signs:

1. **@ Symbol:** Flags URLs containing an `@` symbol because it can make the destination confusing.
2. **Unusually Long URL:** Flags URLs longer than 100 characters.
3. **IP Address:** Flags URLs that use an IPv4-style address instead of a familiar domain name.
4. **Many Hostname Segments:** Flags hostnames containing five or more segments.
5. **Punycode Hostname:** Flags hostnames containing the `xn--` marker, which can represent international characters.
6. **HTTP Scheme:** Flags URLs using HTTP because the connection does not have the transport encryption normally provided by HTTPS.

Additional features:

- Accepts URL text through a command-line interface.
- Handles empty input.
- Handles certain malformed URL formats without crashing.
- Provides explanations of why each detected warning sign matters.
- Allows the user to exit by entering `q`, `quit`, or `exit`.
- Does not visit websites or make network requests.

**Important:** These checks identify warning signs, not confirmed phishing attacks. HTTPS does not guarantee that a website is trustworthy, and the absence of warnings does not prove that a URL is safe.

## Requirements

- Python 3.10 or later
- A terminal or command prompt
- No additional Python packages required

The program uses Python's standard library.

## Project Structure

```text
phishing-url-awareness/
├── screenshots/
│   ├── sample_run.png
│   └── test_results.png
├── tests/
│   └── test_samples.md
├── phishing_checker.py
├── README.md
└── requirements.txt
```

## How to Run

### Windows

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python phishing_checker.py
```

If the `python` command is unavailable, try:

```bash
py phishing_checker.py
```

### macOS or Linux

Open a terminal in the project folder and run:

```bash
python3 phishing_checker.py
```

### Exit the Program

Enter:

```text
q
```

You can also enter `quit` or `exit`.

## Example Output

Example input:

```text
http://192.0.2.10/account
```

Example output:

```text
RESULT:
Review carefully: 2 warning sign(s) found.
- Uses an IP address instead of a familiar domain.
  Why it matters: An IP address instead of a recognizable domain may deserve extra scrutiny.
- Uses HTTP. HTTPS alone does not prove trust.
  Why it matters: HTTP does not encrypt the connection like HTTPS normally does. However, HTTPS does not guarantee that a website is trustworthy.
```

The exact formatting depends on the program's current output.

## Testing

The program is tested using sample URL strings to check whether its warning signs work as expected.

The test records are maintained in `tests/test_samples.md`.

| Test | Input                                     | Expected result                                                                    |
| ---- | ----------------------------------------- | ---------------------------------------------------------------------------------- |
| 1    | `https://www.example.com/login`           | No listed warning signs; the program must clarify that this does not prove safety. |
| 2    | `http://192.0.2.10/account`               | IP-address and HTTP warnings.                                                      |
| 3    | `http://example.com@sample.invalid/login` | @-symbol and HTTP warnings.                                                        |
| 4    | `https://a.b.c.d.e.example.invalid/path`  | Many hostname segments warning.                                                    |
| 5    | `https://xn--example.invalid/`            | Punycode warning.                                                                  |
| 6    | `http://[bad`                             | Malformed URL handled without an unexpected crash.                                 |

The first five cases are the workbook's sample tests. The sixth case checks the malformed-input improvement.

**Testing note:** Record the actual output and PASS or FAIL status in `tests/test_samples.md` after running the program. Do not mark a test as passed unless you have verified its result.

## Screenshots

### Sample Program Run

This screenshot shows the program running and explaining detected URL warning signs.

![Sample run](screenshots/sample_run.png)

### Test Results

This screenshot shows additional URL checks, including malformed URL handling.

![Test results](screenshots/test_results.png)

## Improvements

### 1. Malformed URL Handling

**What changed:** Added `try/except ValueError` around URL parsing.

**Why it matters:** Some malformed URL inputs can cause Python's URL parser to raise an error. Handling that error allows the program to display a helpful message instead of unexpectedly stopping.

**How it is tested:** Enter the sample malformed input `http://[bad` and confirm that the program displays an invalid-format message without crashing. Rerun all five required sample tests to check that the original functionality still works.

### 2. Explanations for Warning Signs

**What changed:** Added a `WARNING_REASONS` dictionary that associates warning messages with explanations. When a warning is detected, the program displays the corresponding reason.

**Why it matters:** Explanations help users understand why a URL pattern deserves attention instead of simply displaying a warning.

**How it is tested:** Run sample URLs that trigger different warning signs and verify that each warning is followed by its explanation. Rerun all five required sample tests.

## Limitations

This project is an educational awareness tool, not a complete phishing detection system.

- It only examines the text entered by the user.
- It does not open URLs or visit websites.
- It does not check website reputation or domain registration.
- It does not scan for malware.
- It does not determine whether a website is legitimate.
- Some legitimate URLs may trigger warnings.
- Some malicious URLs may trigger no warnings.
- HTTPS does not guarantee that a website is safe.
- No listed warning signs does **NOT** mean a URL is safe.

Users should check website addresses carefully and avoid entering sensitive information on unfamiliar or suspicious websites.

## Ethical Use

This project is intended for cybersecurity education and online safety awareness.

- Use sample URL strings for testing.
- Do not collect passwords, OTPs, payment details, or other sensitive information.
- Do not use the project to deceive people.
- Do not test websites or systems without permission.
- Do not treat the program's results as a guarantee of safety.
- Use the tool responsibly to learn about suspicious URL patterns.

## Author

**Shaibanya Dey**

EWB Courses — Cybersecurity Mini Project

**Project:** Phishing URL Awareness Checker
