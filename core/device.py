class NetworkDevice:
    def __init__(self, name, ip, config):
        self.name = name
        self.ip = ip
        self.config = config

    def show_config(self):
        return self.config

    def update_config(self, new_config):
        self.config = new_config