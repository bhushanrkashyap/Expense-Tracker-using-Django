# Expense Tracker

A simple expense tracker web application built with **Django**, using **Django ORM** for database operations, **PostgreSQL** as the backend database engine, and **HTML/CSS** for the UI design.

## Features

- Add, edit, and delete expenses
- Track expense history
- View expenses summary
- Responsive and clean HTML/CSS-based interface
- PostgreSQL database integration for reliable data storage

## Tech Stack

| Technology  | Description                       |
|-------------|-----------------------------------|
| Django      | Python web framework              |
| Django ORM  | Object-Relational Mapper for DB   |
| PostgreSQL  | Database engine                   |
| HTML/CSS    | UI design                         |

## Requirements

- Python ≥ 3.10
- Django ≥ 4.x
- PostgreSQL
- psycopg2-binary (Postgres adapter for Django)

## Setup Instructions

1. **Clone the Repository**
git clone https://github.com/bhushrankashyap/Expense-Tracker-using-Django.git
cd Expense-Tracker-using-Django/track


2. **Create a Virtual Environment**
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. **Install Dependencies**
pip install -r requirements.txt


4. **Configure Database**

- Create a PostgreSQL database and user.
- Update `settings.py` with your Postgres credentials:
  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

5. **Migrate Database**
   python3 manage.py migrate

6. **Run the Server**
python manage.py runserver


7. **Open in Browser**
- Visit: `http://127.0.0.1:8000/`

## Folder Structure

track/
├── pycache/
├── static/
├── templates/
├── init.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py
├── views.py

