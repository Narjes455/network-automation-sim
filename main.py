from core.device_loader import load_devices
from core.simulator import NetworkSimulator
from core.config_manager import save_config
from core.backup_manager import create_backup
from core.logger import log
from core.report_generator import generate_report
from core.diff_engine import compare_configs
from core.alert_manager import create_alert
from core.scheduler import run_scheduler


print("🚀 Starting Network Automation Simulation...")


def backup_job():

    sim = NetworkSimulator()

    devices = load_devices()

    for device in devices:

        # إضافة الجهاز للمحاكي
        sim.add_device(device)

        # حفظ الإعدادات
        save_config(device)

        # إنشاء نسخة احتياطية
        backup_file = create_backup(device)

        # تسجيل العملية
        log(f"Backup created for {device.name}")

        # عرض النتيجة
        print(f"✅ Backup created: {backup_file}")

    # اختبار اكتشاف التغييرات
    with open("data/configs/previous_config.txt", "r") as old_file:
        old_config = old_file.read()

    with open("data/configs/current_config.txt", "r") as new_file:
        new_config = new_file.read()

    changes = compare_configs(old_config, new_config)

    if changes:
        print("⚠ Configuration change detected!")

        alert_file = create_alert(
            "Configuration change detected"
        )

        print(f"🚨 Alert saved: {alert_file}")

        log("ALERT: Configuration change detected")

    # إنشاء التقرير
    report_file = generate_report()

    print(f"\n📄 Change report created: {report_file}")

    print("🎉 All devices processed successfully")


run_scheduler(backup_job)