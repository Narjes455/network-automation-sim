from core.diff_engine import compare_configs
from core.logger import log
import os


def generate_report():

    os.makedirs("data/reports", exist_ok=True)

    with open("data/configs/previous_config.txt", "r", encoding="utf-8") as old_file:
        old_config = old_file.read()

    with open("data/configs/current_config.txt", "r", encoding="utf-8") as new_file:
        new_config = new_file.read()

    differences = compare_configs(old_config, new_config)

    if differences:
        log("ALERT: Configuration change detected")
        print("⚠ Configuration change detected!")
    else:
        print("✅ No configuration changes detected")

    report_path = "data/reports/changes_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:

        report.write("=== Configuration Change Report ===\n\n")

        if differences:
            report.write("Changes Detected:\n\n")

            for line in differences:
                report.write(line + "\n")

        else:
            report.write("No changes detected.\n")

    return report_path