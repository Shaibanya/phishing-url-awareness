import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 45)
    print("   PHISHING URL AWARENESS CHECKER")
    print("=" * 45)
    print("Text checks only. This program does not open websites.")
    print("Enter 'q' to quit.\n")

    while True:
        url = input("Enter a URL to inspect: ").strip()

        if url.lower() in ("q", "quit", "exit"):
            print("Program closed.")
            break

        findings = inspect_url(url)

        print("\nRESULT:")

        if findings == [
            "No listed warning signs found. This does NOT prove safety."
        ]:
            print("No listed warning signs detected.")
        elif findings == ["No URL entered."]:
            print("Please enter a URL.")
        elif findings == ["Could not identify a hostname."]:
            print("Unable to inspect this input.")
        else:
            print(f"Review carefully: {len(findings)} warning sign(s) found.")

        for finding in findings:
            print("- " + finding)

        print("\n" + "-" * 45 + "\n")


if __name__ == "__main__":
    main()