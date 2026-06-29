from core.simulator import NetworkSimulator
from core.device_loader import load_devices
from core.backup_manager import create_backup
from core.config_manager import save_config
from core.logger import log
from core.report_generator import generate_report

print("🚀 Starting Network Automation Simulation...\n")

# إنشاء المحاكي
sim = NetworkSimulator()

# تحميل الأجهزة من ملف JSON
devices = load_devices()

# معالجة الأجهزة
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

# إنشاء تقرير التغييرات
report_file = generate_report()

print(f"\n📄 Change report created: {report_file}")

print("🎉 All devices processed successfully")