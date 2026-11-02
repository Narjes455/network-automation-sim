"""سحب الـ running-config من جهاز Cisco حقيقي وحفظه كنسخة احتياطية بتاريخ ووقت."""
import os
from datetime import datetime

from netmiko import ConnectHandler

from core.ssh_settings import get_ssh_device

device = get_ssh_device()

try:
    print(f"Connecting to {device['host']}...")
    connection = ConnectHandler(**device)
    print("Connected Successfully!")

    config = connection.send_command("show running-config")
    connection.disconnect()

    folder = f"data/backups/{device['host']}"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"{folder}/{timestamp}.txt"

    with open(path, "w", encoding="utf-8") as f:
        f.write(config)

    print(f"Backup Saved: {path}")

except Exception as e:
    print(f"Error: {e}")
