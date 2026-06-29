from core.device_loader import load_devices
from core.simulator import NetworkSimulator
from core.config_manager import save_config
from core.backup_manager import create_backup
from core.logger import log
from core.report_generator import generate_report
from core.scheduler import run_scheduler

print("🚀 Starting Network Automation Simulation...")


def backup_job():

    sim = NetworkSimulator()

    devices = load_devices()

    for device in devices:

        sim.add_device(device)

        save_config(device)

        backup_file = create_backup(device)

        log(f"Backup created for {device.name}")

        print(f"✅ Backup created: {backup_file}")

    report_file = generate_report()

    print(f"\n📄 Change report created: {report_file}")

    print("🎉 All devices processed successfully")


run_scheduler(backup_job)