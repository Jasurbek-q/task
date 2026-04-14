# Task Management Mini App

Django asosida qurilgan to'liq Task Management ilovasi.

## Imkoniyatlar

- **Autentifikatsiya:** Register / Login / Logout
- **Task CRUD:** Yaratish, ko'rish, tahrirlash, o'chirish
- **Maydonlar:** title, description, status, due_date, created_at
- **Filter:** Status bo'yicha filterlash (Pending / In Progress / Done)
- **Frontend:** HTML/CSS (hech qanday framework kerak emas)
- **Database:** PostgreSQL

---

## O'rnatish va Ishga Tushirish

### 1. Reponi clone qilish
```bash
git clone <your-repo-url>
cd taskmanager
```

### 2. Virtual environment yaratish
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. `.env` faylini sozlash
```bash
cp .env .env
```
`.env` faylini oching va quyidagi ma'lumotlarni to'ldiring:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=taskmanager_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. PostgreSQL da database yaratish
```sql
CREATE DATABASE taskmanager_db;
```

### 6. Migratsiyalarni bajarish
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Superyuzer yaratish (ixtiyoriy)
```bash
python manage.py createsuperuser
```

### 8. Serverni ishga tushirish
```bash
python manage.py runserver
```

Brauzerda oching: **http://127.0.0.1:8000**

---

## Loyiha Tuzilmasi

```
taskmanager/
├── manage.py
├── requirements.txt
├── .env.example
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/
    ├── models.py       # Task modeli
    ├── views.py        # Barcha view'lar
    ├── forms.py        # Task va Register formlari
    ├── apps.py
    └── templates/
        └── tasks/
            ├── base.html
            ├── login.html
            ├── register.html
            ├── task_list.html
            ├── task_detail.html
            ├── task_form.html
            └── task_confirm_delete.html
```

---

## Task Statuslari

| Status | Ma'nosi |
|--------|---------|
| Pending | Bajarilmagan |
| In Progress | Jarayonda |
| Done | Bajarilgan |

---

## Texnologiyalar

- Python 3.10+
- Django 4.2
- PostgreSQL
- python-dotenv
