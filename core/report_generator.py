import os

def generate_report():

    os.makedirs("data/reports", exist_ok=True)

    devices = [
        "Router1",
        "Switch1",
        "Firewall1"
    ]

    report_path = "data/reports/changes_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("=========================\n")
        report.write("Network Automation Report\n")
        report.write("=========================\n\n")

        for device in devices:
            report.write(f"- {device}\n")

        report.write(f"\nTotal Devices: {len(devices)}")

    return report_path
