# Phishing URL Awareness Checker

## Overview
A beginner-friendly Python command-line project that checks URLs for selected warning signs associated with potentially suspicious links.

## Features
- Detects the `@` symbol.
- Flags URLs longer than 100 characters.
- Detects IPv4-style hostnames.
- Flags hostnames with five or more segments.
- Detects the `xn--` punycode marker.
- Flags URLs using HTTP.
- Allows multiple URLs to be checked in one session.

## Requirements
- Python 3.10 or newer.
- No external packages required.

## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run `python phishing_checker.py`.
5. Enter a URL to inspect.
6. Enter `q` to exit.

## Testing
Five sample URLs are documented in `tests/test_samples.md`.

## Limitations
This tool inspects URL text only. It does not visit websites, query live threat databases, or guarantee that a URL is safe. It may produce false positives or miss malicious URLs.

## Ethical Use
This project is intended for educational awareness and defensive cybersecurity learning. Do not enter passwords or other sensitive information on suspicious websites.

## Improvements
- Added an interactive loop for checking multiple URLs.
- Added warning-sign counts.
- Added explanatory messages for detected warning signs.