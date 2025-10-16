# 📝 Task Manager

A simple **Django ORM-based project** that allows users to manage their daily tasks easily.  
You can create, view, update, delete, search, and sort tasks using an intuitive web interface.

---

## 🚀 Features

- Create new tasks with title, description, and status  
- Update and delete existing tasks  
- View task details  
- Search tasks by title or description  
- Sort tasks by creation date, status, or title  
- PostgreSQL database integration  
- Django Admin panel for managing data  

---

## 🛠️ Tech Stack

- **Backend:** Django 5  
- **Database:** PostgreSQL  
- **Frontend:** HTML, CSS, Bootstrap  
- **Language:** Python 3  

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Abdelrahman74S/TaskManager.git
cd TaskManager

python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


python manage.py migrate


Then open your browser and go to:
👉 http://127.0.0.1:8000/








