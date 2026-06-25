from core.device import NetworkDevice
from core.simulator import NetworkSimulator
from core.config_manager import save_config
from core.diff_engine import compare_configs
from core.logger import log

# إنشاء محاكي الشبكة
sim = NetworkSimulator()

# جهاز وهمي
device1 = NetworkDevice(
    "Router1",
    "192.168.1.1",
    "interface g0/0\n ip address 192.168.1.1"
)

sim.add_device(device1)

# حفظ config
save_config(device1)
log("Initial config saved")

# تعديل config (محاكاة تغيير شبكات)
old_config = device1.show_config()

device1.update_config(
    "interface g0/0\n ip address 10.0.0.1"
)

new_config = device1.show_config()

# مقارنة التغييرات
changes = compare_configs(old_config, new_config)

for c in changes:
    log(c)
    print(c)