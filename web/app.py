from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route("/")
def dashboard():

    # قراءة الأجهزة
    with open("devices.json", "r") as file:
        devices = json.load(file)

    devices_count = len(devices)

    # حساب النسخ الاحتياطية
    backup_count = 0

    for root, dirs, files in os.walk("data/backups"):
        backup_count += len(files)

    # حساب التنبيهات
    alerts_count = 0

    alerts_file = "data/reports/alerts.txt"

    if os.path.exists(alerts_file):
        with open(alerts_file, "r") as file:
            alerts_count = len(file.readlines())

    return render_template(
        "index.html",
        devices=devices_count,
        backups=backup_count,
        alerts=alerts_count
    )


@app.route("/devices")
def devices_page():

    with open("devices.json", "r") as file:
        devices = json.load(file)

    html = """
    <h1>🌐 Network Devices</h1>
    <hr>
    """

    for device in devices:

        html += f"""
        <h3>{device['name']}</h3>

        <ul>
            <li><strong>IP:</strong> {device['ip']}</li>
            <li><strong>Type:</strong> {device['type']}</li>
        </ul>

        <hr>
        """

    return html


if __name__ == "__main__":
    app.run(debug=True)