from core.device import NetworkDevice

class NetworkSimulator:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_device(self, name):
        for d in self.devices:
            if d.name == name:
                return d
        return None