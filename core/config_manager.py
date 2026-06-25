import os

def save_config(device):
    os.makedirs("data/configs", exist_ok=True)

    file_path = f"data/configs/{device.name}.txt"
    with open(file_path, "w") as f:
        f.write(device.config)

    return file_path