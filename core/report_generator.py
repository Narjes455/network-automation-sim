from core.diff_engine import compare_configs


def generate_report():

    with open("data/configs/previous_config.txt", "r") as old_file:
        old_config = old_file.read()

    with open("data/configs/current_config.txt", "r") as new_file:
        new_config = new_file.read()

    differences = compare_configs(old_config, new_config)

    report_path = "data/reports/changes_report.txt"

    with open(report_path, "w") as report:

        report.write("=== Configuration Change Report ===\n\n")

        if differences:
            for line in differences:
                report.write(line + "\n")
        else:
            report.write("No changes detected.\n")

    return report_path