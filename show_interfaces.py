from netmiko import ConnectHandler

router = {
    "device_type": "cisco_xe",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
}

try:
    print("Connecting...")

    conn = ConnectHandler(**router)

    output = conn.send_command("show version")

    print(output)

    conn.disconnect()

except Exception as e:
    print(f"Error: {e}")