import requests
from modules.payload_generator import generate_payloads
from utils.http_handler import send_payload

def scan_for_vuln(url):
    payloads = generate_payloads()
    for payload in payloads:
        response = send_payload(url, payload)
        if "expected response" in response.text.lower():
            return f"[+] Vulnerability Found with payload: {payload}"
    return "[-] No Blind SQLi vulnerability detected"