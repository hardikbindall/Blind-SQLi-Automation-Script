def give_recommendations(url):
    return (
        "Security Recommendations:\n"
        "- Use Prepared Statements\n"
        "- Sanitize User Inputs\n"
        "- Disable SQL error messages in response\n"
        "- Implement Web Application Firewall\n"
        f"- Monitor traffic to {url} for anomalous patterns\n"
    )