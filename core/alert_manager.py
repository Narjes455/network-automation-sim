from datetime import datetime
import os


def create_alert(message):
    os.makedirs("data/reports", exist_ok=True)

    alert_file = "data/reports/alerts.txt"

    with open(alert_file, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] ALERT: {message}\n")

    return alert_file