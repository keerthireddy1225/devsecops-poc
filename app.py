import requests

# GitHub details
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
OWNER = "YOUR_ORG_OR_USERNAME"
REPO = "YOUR_REPOSITORY"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

base_url = f"https://api.github.com/repos/{OWNER}/{REPO}"

# -----------------------------
# Dependabot Alerts
# -----------------------------
print("\n===== DEPENDABOT ALERTS =====")
url = f"{base_url}/dependabot/alerts"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    alerts = response.json()
    for alert in alerts:
        print(f"Severity : {alert['security_vulnerability']['severity']}")
        print(f"Package  : {alert['dependency']['package']['name']}")
        print(f"State    : {alert['state']}")
        print("-" * 50)
else:
    print(response.status_code, response.text)

# -----------------------------
# Secret Scanning Alerts
# -----------------------------
print("\n===== SECRET SCANNING ALERTS =====")
url = f"{base_url}/secret-scanning/alerts"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    alerts = response.json()
    for alert in alerts:
        print(f"Secret Type : {alert['secret_type']}")
        print(f"State       : {alert['state']}")
        print(f"Created At  : {alert['created_at']}")
        print("-" * 50)
else:
    print(response.status_code, response.text)

# -----------------------------
# Code Scanning Alerts
# -----------------------------
print("\n===== CODE SCANNING ALERTS =====")
url = f"{base_url}/code-scanning/alerts"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    alerts = response.json()
    for alert in alerts:
        print(f"Rule      : {alert['rule']['id']}")
        print(f"Severity  : {alert['rule']['severity']}")
        print(f"State     : {alert['state']}")
        print(f"File      : {alert['most_recent_instance']['location']['path']}")
        print("-" * 50)
else:
    print(response.status_code, response.text)
