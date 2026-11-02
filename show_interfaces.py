"""عرض حالة الواجهات في جهاز Cisco حقيقي (show ip interface brief)."""
from netmiko import ConnectHandler

from core.ssh_settings import get_ssh_device

device = get_ssh_device()

try:
    print(f"Connecting to {device['host']}...")
    conn = ConnectHandler(**device)

    print(conn.send_command("show ip interface brief"))

    conn.disconnect()

except Exception as e:
    print(f"Error: {e}")
