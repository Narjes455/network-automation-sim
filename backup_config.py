from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
}

print("Connecting...")

connection = ConnectHandler(**device)

print("Connected Successfully!")

output = connection.send_command("show version")

print(output)

connection.disconnect()