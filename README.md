# Django REST Framework Assignment

This project demonstrates a simple **School Management API** built using **Django** and **Django REST Framework (DRF)**.  
It provides endpoints to manage students and teachers with proper validation and error handling.

---

## 🚀 Setup Instructions

1.**Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows

2.**Install dependencies**
   ```bash
   pip install django djangorestframework

3.**Configure settings**
   Add 'rest_framework' and 'school' to INSTALLED_APPS in settings.py.

4.**Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5.**Start the server**
   ```bash
   python manage.py runserver
