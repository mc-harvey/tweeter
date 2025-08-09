Tweeter is a simple Twitter-style Django web app that allows users to post short messages (tweets) up to 280 characters with an optional image.
It features a built-in banned words filter, user authentication, and a clean Bootstrap-styled interface served from local static files (no CDN).
Perfect as a beginner Django project to learn about forms, file uploads, static files, and basic CRUD functionality.

Features
Post tweets with up to 280 characters.
Optionally attach an image to your tweet.
Offensive word filtering.
Local Bootstrap styling (no internet connection required).
Responsive UI for desktop and mobile.

Requirements
Make sure you have:
Python 3.10+
Django 5.x (installed via requirements.txt)
Git

How to Create a Tweet
Open your browser and go to http://127.0.0.1:8000/.
Click + New Tweet.
Type your tweet (max 280 characters).
Optionally attach an image.
Click Send.
Your tweet will appear in the timeline.

tweeter/
│── manage.py
│── requirements.txt
│── .gitignore
│── tweeter/          # Project settings
│── tweets/           # Main app
│   ├── static/       # Bootstrap CSS/JS
│   ├── templates/    # HTML templates
│   ├── models.py     # Tweet model
│   ├── forms.py      # Tweet form
│   ├── views.py      # Logic
│   ├── urls.py       # Routes

venv/
db.sqlite3
__pycache__/
*.pyc
