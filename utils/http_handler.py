import requests

def send_payload(url, payload):
    try:
        params = {"input": payload}
        response = requests.get(url, params=params, timeout=10)
        return response
    except requests.exceptions.RequestException as e:
        return str(e)