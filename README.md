# ConnectHub - Social Media Platform

## Project Overview

ConnectHub is a full-stack social media platform developed using Django, HTML, CSS, and JavaScript.

The platform allows users to create accounts, create and share posts, upload images, like posts, comment on posts, follow other users, search for users, explore content, and receive notifications.

This project was developed as part of a Full Stack Development project.

---

## Features

- User Registration
- User Login and Logout
- User Profiles
- Create Posts
- Upload Post Images
- Like and Unlike Posts
- Comment on Posts
- Follow and Unfollow Users
- Search Users
- Explore Users and Posts
- Notifications
- Responsive User Interface
- SQLite Database
- Django Admin Panel

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Django

### Database

- SQLite

### Additional Library

- Pillow

---

## Project Structure

```text
social-media-platform/
│
├── social/
│   ├── migrations/
│   ├── templates/
│   │   └── social/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── create_post.html
│   │       ├── profile.html
│   │       ├── explore.html
│   │       ├── search.html
│   │       └── notifications.html
│   │
│   ├── static/
│   │   └── social/
│   │       └── style.css
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── socialmedia/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md