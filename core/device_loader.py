import json
from core.device import NetworkDevice


def load_devices():

    with open("devices.json", "r") as f:
        devices_data = json.load(f)

    devices = []

    for d in devices_data:

        device = NetworkDevice(
            d["name"],
            d["ip"],
            d["config"]
        )

        devices.append(device)

    return devices