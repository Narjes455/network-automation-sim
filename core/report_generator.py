import os
from datetime import datetime


def generate_report(changes):
    """changes: قاموس {اسم الجهاز: قائمة أسطر الفرق}"""

    os.makedirs("data/reports", exist_ok=True)

    report_path = "data/reports/changes_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:

        report.write("=== Configuration Change Report ===\n")
        report.write(f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n")

        if not changes:
            report.write("No changes detected.\n")

        for device_name, diff in changes.items():
            report.write(f"--- {device_name} ---\n")
            for line in diff:
                report.write(line + "\n")
            report.write("\n")

    return report_path
