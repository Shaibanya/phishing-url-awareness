from flask import Flask, request, render_template_string
from phishing_checker import inspect_url, WARNING_REASONS

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing URL Awareness Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            color: #172033;
            margin: 0;
            padding: 30px 16px;
        }
        .container {
            max-width: 700px;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 8px 28px #00000012;
        }
        h1 { color: #1746a2; }
        p { line-height: 1.6; }
        input {
            box-sizing: border-box;
            width: 100%;
            padding: 14px;
            margin: 12px 0;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 14px;
            background: #1746a2;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover { background: #10357e; }
        .result {
            margin-top: 24px;
            padding: 18px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            overflow-wrap: anywhere;
        }
        .warning { margin: 16px 0; }
        .reason { color: #475569; margin-top: 6px; }
        .notice {
            margin-top: 24px;
            padding: 14px;
            background: #fff7ed;
            border-radius: 8px;
            font-size: 14px;
        }
        footer {
            margin-top: 25px;
            color: #64748b;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <main class="container">
        <h1>Phishing URL Awareness Checker</h1>
        <p>
            Check a URL for common phishing warning signs.
            This tool examines the text you enter and does not visit the website.
        </p>

        <form method="POST">
            <label for="url"><strong>Enter a URL to inspect</strong></label>
            <input
                id="url"
                name="url"
                type="text"
                placeholder="https://example.com/login"
                value="{{ url }}"
                required
            >
            <button type="submit">Check URL</button>
        </form>

        {% if checked %}
        <section class="result" aria-live="polite">
            <h2>Results</h2>
            {% if findings %}
                {% for finding in findings %}
                <div class="warning">
                    <strong>{{ finding }}</strong>
                    {% if finding in reasons %}
                    <p class="reason">
                        <strong>Why it matters:</strong>
                        {{ reasons[finding] }}
                    </p>
                    {% endif %}
                </div>
                {% endfor %}
            {% endif %}
        </section>
        {% endif %}

        <div class="notice">
            <strong>Important:</strong> These are warning signs, not proof
            of a phishing attack. No warnings do not mean a URL is safe.
            HTTPS also does not guarantee that a website is trustworthy.
        </div>

        <footer>
            Educational cybersecurity project by Shaibanya Dey · EWB Courses
        </footer>
    </main>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    url = ""
    findings = []
    checked = False

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        checked = True

        if url:
            findings = inspect_url(url)
        else:
            findings = ["No URL entered."]

    return render_template_string(
        HTML,
        url=url,
        findings=findings,
        reasons=WARNING_REASONS,
        checked=checked,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)