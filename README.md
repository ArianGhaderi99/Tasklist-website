TaskFlow - Task Manager Application

https://github.com/ArianGhaderi99/Tasklist-website/blob/main/Screenshot%202026-06-11%20203536.png


📝 About

TaskFlow is a modern, lightweight task management web application built with Django. It allows users to register, log in, and manage their personal tasks with due dates and times. Each user has their own isolated task list. The UI is fully responsive, clean, and minimalist – works on desktop, tablet, and mobile.

✨ Features

· 🔐 User Authentication – Registration, login, logout (Django built-in)
· ✅ Personal Task Management – Each user sees only their own tasks
· 📅 Due Date & Time – Set deadlines for each task
· ✔️ Mark as Completed – Toggle task status with one click
· 🗑️ Delete & Edit – Full CRUD operations
· 🎨 Responsive Design – CSS Grid/Flexbox, mobile-friendly layout
· 💾 Persistent Storage – All data stored in database (SQLite/PostgreSQL)
· 🛡️ Secure – CSRF protection, login required for task operations

🖼️ Screenshots

Replace screenshots/task-page.png with an actual screenshot of the task management page.

🚀 Tech Stack

· Backend: Django 4.x (Python 3.10+)
· Frontend: HTML5, CSS3, JavaScript (vanilla)
· Database: SQLite (default), can be switched to PostgreSQL/MySQL
· Authentication: Django's built-in auth system

📁 Project Structure

```
taskflow/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── task/                     # main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── migrations/
│   ├── templates/task/
│   │   ├── task_list.html
│   │   └── task_form.html
│   └── static/task/css/
│       ├── common.css
│       └── task.css
├── accounts/                 # auth app
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/accounts/
│       └── login.html
├── static/
├── templates/
│   └── base.html
└── screenshots/              # (create this folder)
    └── task-page.png
```

🔧 Installation & Setup

Prerequisites

· Python 3.10+
· pip
· virtualenv (optional but recommended)

Steps

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/taskflow.git
   cd taskflow
   ```
2. Create virtual environment & activate
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create superuser (optional, for admin panel)
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server
   ```bash
   python manage.py runserver
   ```
7. Open http://127.0.0.1:8000/ in your browser.


🧪 Usage

· Register a new account (username + password).
· Login with your credentials.
· Add a task – fill title, due date, due time (optional).
· View tasks – all your tasks appear in a list.
· Mark as done – click the checkbox to toggle completion.
· Edit – click the edit (✏️) icon.
· Delete – click the trash (🗑️) icon and confirm.
· Logout – from the navigation bar.

🛠️ Customization

· Styles: Edit static/task/css/common.css and task.css.
· Password validators: Adjust AUTH_PASSWORD_VALIDATORS in settings.py to relax or strengthen password rules.
· Database: Change DATABASES in settings.py to use PostgreSQL/MySQL.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📄 License

MIT

👨‍💻 Author

Your Name – ArianGhaderi99

---

Enjoy managing your tasks with TaskFlow! 🎉
