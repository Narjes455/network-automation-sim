# 🌐 Network Automation & Configuration Backup System

مشروع متكامل لأتمتة الشبكات باستخدام Python، بدأ كمحاكاة تعليمية ثم تطور للاتصال الحقيقي بأجهزة Cisco عبر SSH وإنشاء نسخ احتياطية للإعدادات وإدارة عمليات الشبكة بشكل آلي.

---

# 📌 فكرة المشروع

يهدف المشروع إلى تبسيط إدارة الشبكات من خلال أتمتة المهام المتكررة مثل:

* إدارة أجهزة الشبكة
* حفظ إعدادات الأجهزة
* إنشاء نسخ احتياطية تلقائية
* اكتشاف التغييرات في الإعدادات
* إنشاء التقارير والتنبيهات
* جدولة المهام الدورية
* عرض حالة النظام عبر Web Dashboard
* الاتصال الحقيقي بأجهزة Cisco عبر SSH

---

# 🛠️ التقنيات المستخدمة

* Python 3
* Flask
* Netmiko
* Paramiko
* JSON
* OOP
* Logging
* Difflib
* Schedule
* HTML
* CSS

---

# 📦 تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

---

# 📁 هيكل المشروع

```text
network-automation-sim
│
├── main.py                 # تشغيل المحاكاة (فحص + نسخ احتياطي + تنبيهات + جدولة)
├── devices.json            # قائمة الأجهزة المحاكاة (الاسم، IP، النوع، الإعدادات)
├── .env.example            # نموذج بيانات الاتصال بالجهاز الحقيقي
│
├── connect_device.py       # جهاز حقيقي: اختبار الاتصال + show version
├── show_interfaces.py      # جهاز حقيقي: show ip interface brief
├── backup_config.py        # جهاز حقيقي: نسخة احتياطية من running-config
│
├── core/
│   ├── device.py           # كلاس الجهاز
│   ├── device_loader.py    # تحميل الأجهزة من devices.json
│   ├── simulator.py        # المحاكي
│   ├── config_manager.py   # حفظ الإعدادات الحالية
│   ├── backup_manager.py   # النسخ الاحتياطية وآخر نسخة لكل جهاز
│   ├── diff_engine.py      # مقارنة الإعدادات (difflib)
│   ├── alert_manager.py    # التنبيهات
│   ├── report_generator.py # تقرير التغييرات
│   ├── scheduler.py        # الجدولة كل دقيقة
│   ├── ssh_settings.py     # قراءة بيانات SSH من .env
│   └── logger.py           # السجل
│
├── web/                    # لوحة التحكم (Flask)
│   ├── app.py
│   ├── templates/index.html
│   └── static/style.css
│
└── data/
    ├── configs/            # الإعدادات الحالية لكل جهاز
    ├── backups/            # تنشأ تلقائياً (مستثناة من Git)
    └── reports/            # تنشأ تلقائياً (مستثناة من Git)
```

---

# ▶️ تشغيل المشروع

## تشغيل المحاكاة مع الجدولة (كل دقيقة)

```bash
python main.py
```

## تشغيل الفحص مرة وحدة فقط

```bash
python main.py --once
```

> جربي تعدلين إعدادات أي جهاز في `devices.json` وتشغلين مرة ثانية: النظام بيكتشف التغيير، ويسوي نسخة احتياطية جديدة، ويسجل تنبيه، ويطلع تقرير بالفرق.

## الاتصال بجهاز Cisco حقيقي

انسخي `.env.example` باسم `.env` وعبّي بيانات الجهاز (الملف مستثنى من Git فما تنرفع كلمة المرور):

```bash
cp .env.example .env
python connect_device.py     # اختبار الاتصال
python show_interfaces.py    # حالة الواجهات
python backup_config.py      # نسخة احتياطية من الإعدادات
```

يمكن التجربة على Cisco DevNet Sandbox المجاني.

## تشغيل لوحة التحكم

```bash
python web/app.py
```

ثم:

```text
http://127.0.0.1:5000
```

---

# 📊 المميزات الحالية

### إدارة الشبكات

✅ إدارة أجهزة متعددة

✅ تحميل الأجهزة من JSON

✅ تنظيم الأجهزة داخل المشروع

---

### النسخ الاحتياطية

✅ إنشاء نسخ احتياطية

✅ حفظ الإعدادات تلقائياً

✅ تخزين ملفات Backup


---

### إدارة الإعدادات

✅ حفظ Configuration

✅ مقارنة الإعدادات

✅ اكتشاف التغييرات

✅ إنشاء تقارير للتعديلات

---

### التنبيهات

✅ تنبيهات عند اكتشاف تغييرات

✅ تسجيل وقت التنبيه

✅ إنشاء alerts.txt

---

### التقارير

✅ إنشاء تقارير تلقائية

✅ حفظ التقارير داخل مجلد مستقل

---

### الأتمتة

✅ جدولة المهام

✅ تنفيذ النسخ الاحتياطية دورياً

✅ أتمتة العمليات المتكررة

---

### واجهة الويب

✅ Flask Dashboard

✅ عرض عدد الأجهزة

✅ عرض عدد النسخ الاحتياطية

✅ عرض عدد التنبيهات

---

### الاتصال الحقيقي بالشبكات

✅ الاتصال بأجهزة Cisco الحقيقية

✅ SSH باستخدام Netmiko

✅ تنفيذ أوامر Cisco مباشرة

✅ سحب Running Configuration

✅ عرض حالة الواجهات

✅ حفظ إعدادات الراوتر الحقيقية

---

# 🆕 الإصدار الأول (v1)

* إنشاء الهيكل الأساسي للمشروع
* محاكاة أجهزة الشبكة

# 🆕 الإصدار الثاني (v2)

* دعم أجهزة متعددة
* تحميل الأجهزة من JSON

# 🆕 الإصدار الثالث (v3)

* إنشاء التقارير التلقائية

# 🆕 الإصدار الرابع (v4)

* مقارنة الإعدادات باستخدام Difflib

# 🆕 الإصدار الخامس (v5)

* تحسين تقارير التغييرات

# 🆕 الإصدار السادس (v6)

* جدولة المهام باستخدام Schedule

# 🆕 الإصدار السابع (v7)

* نظام التنبيهات الآلي

# 🆕 الإصدار الثامن (v8)

* Web Dashboard باستخدام Flask

# 🆕 الإصدار التاسع (v9)

* الاتصال الحقيقي بأجهزة Cisco
* استخدام Netmiko
* تنفيذ أوامر Cisco عبر SSH
* عرض معلومات الواجهات
* سحب Running Configuration
* حفظ النسخة الاحتياطية من الجهاز الحقيقي
* الانتقال من المحاكاة إلى بيئة شبكات حقيقية

---

# 🆕 الإصدار العاشر (v10)

* إصلاح تحميل الأجهزة (devices.json رجع قائمة أجهزة)
* نقل بيانات SSH إلى ملف .env بدل كتابتها في الكود
* مقارنة إعدادات كل جهاز مع آخر نسخة احتياطية له
* نسخة احتياطية جديدة وتنبيه فقط عند وجود تغيير
* تقرير تغييرات لكل الأجهزة
* خيار `--once` للتشغيل مرة وحدة
* تصحيح سكربتات الاتصال الحقيقي (show version / show ip interface brief / backup)

---

# 🚀 التطويرات القادمة (v11)

* دمج الاتصال الحقيقي داخل Dashboard
* إضافة زر Backup من الواجهة
* إضافة Device Inventory
* إدارة أكثر من جهاز Cisco
* قاعدة بيانات SQLite
* تسجيل المستخدمين
* صلاحيات متعددة
* Telegram Alerts
* Email Alerts
* PDF Reports
* REST API
* Docker Deployment

---

# 🎯 المهارات المكتسبة

* Network Automation
* Cisco Networking
* SSH Automation
* Python Programming
* Flask Development
* Configuration Management
* Backup Systems
* Change Detection
* Network Monitoring
* Infrastructure Automation

---

# 👩‍💻 المطورة

نرجس حسن العمري

دبلوم إدارة أنظمة الشبكات

الاهتمامات:

* Network Automation
* Cybersecurity
* Python Development
* Infrastructure Management
* Smart Network Solutions


[🔗 LinkedIn](https://www.linkedin.com/in/%D9%86%D8%B1%D8%AC%D8%B3-%D8%A7%D9%84%D8%B9%D9%85%D8%B1%D9%8A-757b68273/)

[🐙 GitHub](https://github.com/Narjes455)

---

> المشروع قيد التطوير المستمر، ويتم تحديثه تدريجياً لإضافة مزيد من خصائص أتمتة الشبكات وإدارة البنية التحتية.
