"""اختبار الاتصال بجهاز Cisco حقيقي عبر SSH وعرض معلومات الجهاز (show version)."""
from netmiko import ConnectHandler

from core.ssh_settings import get_ssh_device

device = get_ssh_device()

try:
    print(f"Connecting to {device['host']}...")
    connection = ConnectHandler(**device)
    print("Connected Successfully!")

    print(connection.send_command("show version"))

    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")
