"""قراءة بيانات الاتصال بجهاز Cisco الحقيقي من متغيرات البيئة (ملف .env).

بهذي الطريقة ما تنكتب كلمة المرور داخل الكود ولا تنرفع على GitHub.
"""
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_ssh_device():
    host = os.getenv("CISCO_HOST")
    username = os.getenv("CISCO_USERNAME")
    password = os.getenv("CISCO_PASSWORD")

    if not (host and username and password):
        raise SystemExit(
            "❌ بيانات الاتصال ناقصة. انسخي .env.example باسم .env "
            "وعبّي CISCO_HOST و CISCO_USERNAME و CISCO_PASSWORD"
        )

    return {
        "device_type": os.getenv("CISCO_DEVICE_TYPE", "cisco_xe"),
        "host": host,
        "username": username,
        "password": password,
        "port": int(os.getenv("CISCO_PORT", "22")),
    }
