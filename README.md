# 🗂️ Task Manager

**Task Manager** is a web application for managing tasks, built with Django.  
It allows users to create, view, update, and delete tasks, assign them to workers,  
and see tasks where the user is either the sole assignee or one of multiple collaborators.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/HappyDen08/task-manager.git
cd task-manager
git checkout develop
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Load the fixture data

```bash
python manage.py loaddata initial_data.json
```

### 7. Start the development server

```bash
python manage.py runserver
```

📍 Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ Features

- 🔐 Authentication: login/logout/redirects
- 👷 Workers: worker list, profile pages
- ✅ My Tasks: tasks where the user is the only assignee
- 🤝 Shared Tasks: tasks with two or more assignees
- ✍️ Create and update tasks
- 🗑️ Delete tasks
- 🔎 Search tasks by name and assignee
- 🪄 Bootstrap 5 UI
- ♻️ Toggle task completion status

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Django 5
- **Frontend**: HTML, CSS, Bootstrap 5
- **Extras**: HTMX (for dynamic updates), SQLite

## 🧪 Testing

Tests for models and views can be found in `task/tests/`. To run tests:

```bash
python manage.py test
```

---


## 🧩 Optional Features

- [x] Task search
- [x] Pagination
- [x] Task priority levels
- [x] Separation of “My Tasks” and “Shared Tasks”

---


## 🧠 Author

- GitHub: [HappyDen08](https://github.com/HappyDen08)
- Django Project: _Task Manager_

---

## 📜 License

This project is part of a learning task and is intended for educational purposes.
