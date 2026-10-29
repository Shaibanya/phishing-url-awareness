
import re
from urllib.parse import urlparse


# Improvement 2: Explain why each warning sign matters.
WARNING_REASONS = {
    "Contains an @ symbol; inspect carefully.":
        "The @ symbol can make part of a URL look like the website name "
        "when it is actually user information.",

    "Unusually long URL (over 100 characters).":
        "An unusually long URL can hide confusing or misleading details.",

    "Uses an IP address instead of a familiar domain.":
        "An IP address instead of a recognizable domain may deserve "
        "extra scrutiny.",

    "Contains many hostname segments/subdomains.":
        "Many hostname segments can make it harder to recognize "
        "the actual website domain.",

    "Contains a punycode-style hostname.":
        "Punycode can represent international characters that may "
        "look similar to characters in another domain.",

    "Uses HTTP. HTTPS alone does not prove trust.":
        "HTTP does not encrypt the connection like HTTPS normally does. "
        "However, HTTPS does not guarantee that a website is trustworthy.",
}


def inspect_url(raw_url):
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Improvement 1: Handle malformed URLs without crashing.
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: URL length
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IPv4-style hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Many hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode marker
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

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

        elif findings == ["This text is not a valid URL format."]:
            print("Unable to inspect this malformed URL.")

        else:
            print(
                f"Review carefully: {len(findings)} warning sign(s) found."
            )

        for finding in findings:
            print("- " + finding)

            # Display the reason associated with each warning.
            if finding in WARNING_REASONS:
                print("  Why it matters: " + WARNING_REASONS[finding])

        print("\n" + "-" * 45 + "\n")


if __name__ == "__main__":
    main()
