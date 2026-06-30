from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
}

print("Connecting...")

connection = ConnectHandler(**device)

print("Connected Successfully!")

config = connection.send_command("show running-config")

with open("backup.txt", "w", encoding="utf-8") as f:
    f.write(config)

print("Backup Saved!")

connection.disconnect()