import os
from datetime import datetime


def create_backup(device):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    folder = f"data/backups/{device.name}"

    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/{timestamp}.txt"

    # لو انعملت نسختين بنفس الثانية ما تنكتب وحدة فوق الثانية
    counter = 1
    while os.path.exists(filename):
        filename = f"{folder}/{timestamp}_{counter}.txt"
        counter += 1

    with open(filename, "w", encoding="utf-8") as f:
        f.write(device.config)

    return filename


def get_latest_backup(device):
    """ترجع محتوى آخر نسخة احتياطية للجهاز، أو None إذا ما فيه نسخ."""

    folder = f"data/backups/{device.name}"

    if not os.path.isdir(folder):
        return None

    files = sorted(f for f in os.listdir(folder) if f.endswith(".txt"))

    if not files:
        return None

    with open(f"{folder}/{files[-1]}", "r", encoding="utf-8") as f:
        return f.read()
