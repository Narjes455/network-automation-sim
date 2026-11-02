import argparse

from core.device_loader import load_devices
from core.simulator import NetworkSimulator
from core.config_manager import save_config
from core.backup_manager import create_backup, get_latest_backup
from core.logger import log
from core.report_generator import generate_report
from core.diff_engine import compare_configs
from core.alert_manager import create_alert
from core.scheduler import run_scheduler


def backup_job():

    sim = NetworkSimulator()
    changes = {}

    for device in load_devices():

        # إضافة الجهاز للمحاكي وحفظ إعداداته الحالية
        sim.add_device(device)
        save_config(device)

        # مقارنة الإعدادات الحالية مع آخر نسخة احتياطية
        last_backup = get_latest_backup(device)

        if last_backup is None:
            backup_file = create_backup(device)
            log(f"First backup created for {device.name}")
            print(f"✅ {device.name}: first backup -> {backup_file}")
            continue

        diff = compare_configs(last_backup, device.config)

        if diff:
            changes[device.name] = diff
            backup_file = create_backup(device)
            create_alert(f"Configuration change detected on {device.name}")
            log(f"ALERT: Configuration change detected on {device.name}")
            print(f"⚠ {device.name}: change detected, new backup -> {backup_file}")
        else:
            print(f"✔ {device.name}: no changes")

    report_file = generate_report(changes)
    print(f"📄 Change report: {report_file}")
    print("🎉 All devices processed successfully\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Network Automation Simulation")
    parser.add_argument(
        "--once",
        action="store_true",
        help="تشغيل الفحص مرة وحدة بدون جدولة",
    )
    args = parser.parse_args()

    print("🚀 Starting Network Automation Simulation...")

    backup_job()

    if not args.once:
        run_scheduler(backup_job)
