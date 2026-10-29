# Phishing URL Awareness Checker — Test Results

## Test 1: Normal HTTPS URL

- **Input:** `https://www.example.com/login`
- **Expected:** No listed warning signs detected.
- **Actual:** No listed warning signs detected.
- **Status:** PASS

## Test 2: IP Address and HTTP

- **Input:** `http://192.0.2.10/account`
- **Expected:** Detect an IP address and HTTP.
- **Actual:** Both warning signs detected.
- **Status:** PASS

## Test 3: @ Symbol

- **Input:** `http://example.com@sample.invalid/login`
- **Expected:** Detect the @ symbol and HTTP.
- **Actual:** Both warning signs detected.
- **Status:** PASS

## Test 4: Multiple Hostname Segments

- **Input:** `https://a.b.c.d.e.example.invalid/path`
- **Expected:** Detect many hostname segments.
- **Actual:** Warning detected.
- **Status:** PASS

## Test 5: Punycode

- **Input:** `https://xn--example.invalid/`
- **Expected:** Detect the punycode-style hostname.
- **Actual:** Warning detected.
- **Status:** PASS

## Limitations

The checker inspects URL text only. It does not visit websites or guarantee that a URL is safe.
