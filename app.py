import requests

# -----------------------------
# Dummy GitHub Details
# -----------------------------
GITHUB_TOKEN = "ghp_dummy1234567890abcdef"
OWNER = "contoso-security"
REPO = "sample-application"

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

    if not alerts:
        print("No Dependabot alerts found")

    for alert in alerts:
        print(f"""
Alert Number : {alert['number']}
Package      : {alert['dependency']['package']['name']}
Severity     : {alert['security_vulnerability']['severity']}
State        : {alert['state']}
Created      : {alert['created_at']}
""")
else:
    print("Dependabot API Error:")
    print(response.status_code, response.text)


# -----------------------------
# Secret Scanning Alerts
# -----------------------------
print("\n===== SECRET SCANNING ALERTS =====")

url = f"{base_url}/secret-scanning/alerts"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    alerts = response.json()

    if not alerts:
        print("No Secret Scanning alerts found")

    for alert in alerts:
        print(f"""
Alert Number : {alert['number']}
Secret Type  : {alert['secret_type']}
State        : {alert['state']}
Created      : {alert['created_at']}
""")

else:
    print("Secret Scanning API Error:")
    print(response.status_code, response.text)


# -----------------------------
# Code Scanning Alerts
# -----------------------------
print("\n===== CODE SCANNING ALERTS =====")

url = f"{base_url}/code-scanning/alerts"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    alerts = response.json()

    if not alerts:
        print("No Code Scanning alerts found")

    for alert in alerts:
        instance = alert.get("most_recent_instance", {})

        print(f"""
Alert Number : {alert['number']}
Rule ID      : {alert['rule']['id']}
Severity     : {alert['rule']['security_severity_level']}
State        : {alert['state']}
File         : {instance.get('location', {}).get('path')}
Created      : {alert['created_at']}
""")

else:
    print("Code Scanning API Error:")
    print(response.status_code, response.text)
