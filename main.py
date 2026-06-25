from core.simulator import NetworkSimulator
from core.device_loader import load_devices
from core.backup_manager import create_backup
from core.config_manager import save_config
from core.logger import log

# إنشاء المحاكي
sim = NetworkSimulator()

# تحميل الأجهزة من devices.json
devices = load_devices()

for device in devices:

    sim.add_device(device)

    # حفظ الإعدادات
    save_config(device)

    # إنشاء نسخة احتياطية
    backup_file = create_backup(device)

    log(f"Backup created for {device.name}")

    print(f"✅ Backup created: {backup_file}")

print("\n🎉 All devices processed successfully")
