from datetime import datetime


def log(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("reports/log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")