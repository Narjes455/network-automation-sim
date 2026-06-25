import os
from datetime import datetime


def create_backup(device):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    folder = f"data/backups/{device.name}"

    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(device.config)

    return filename