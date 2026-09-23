# 🌐 ConnectHub - Social Media Platform

ConnectHub is a full-stack social media web application developed as part of a Full Stack Development Internship Task.

The application allows users to create accounts, create and share posts, upload images, like posts, comment on posts, follow other users, search for users, explore content, and receive notifications.

---

## 🚀 Features

- 👤 User Registration
- 🔐 User Login and Logout
- 👤 User Profiles
- 📝 Create Posts
- 🖼️ Upload Post Images
- ❤️ Like and Unlike Posts
- 💬 Comment on Posts
- 👥 Follow and Unfollow Users
- 🔎 Search Users
- 🌎 Explore Users and Posts
- 🔔 Notifications
- 📱 Responsive Design
- 🗄️ SQLite Database
- 👨‍💼 Django Admin Panel
- ✨ Interactive User Interface

---

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Django
- **Database:** SQLite
- **Image Handling:** Pillow
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
social-media-platform/
│
├── social/
│   ├── migrations/
│   │
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
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
---

## 👨‍💼 Admin Panel

The Django admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
---

## 🌐 How the Application Works

### 1. Home Page

Users can view posts created by users and interact with posts using likes and comments.

### 2. User Registration

New users can create an account using a username and password.

A profile is automatically created for the registered user.

### 3. Login

Registered users can securely log in to the application.

### 4. Create Post

Logged-in users can:

- Create posts
- Write post content
- Upload images
- Publish posts

### 5. Like and Comment

Users can like or unlike posts and add comments to posts.

### 6. Follow Users

Users can follow or unfollow other users.

Following a user generates a notification for the followed user.

### 7. Explore

The Explore page allows users to discover:

- Other users
- Recent posts

### 8. Search

Users can search for other users by username.

### 9. Notifications

Users receive notifications for activities such as:

- Likes
- Comments
- New Followers

### 10. Profile

The profile page displays:

- Username
- Bio
- User posts
- Followers
- Following count

---
---

## 🗄️ Database Models

The application uses the following main models.

### Profile

Stores:

- User
- Bio
- Profile Image

### Post

Stores:

- User
- Post Content
- Post Image
- Created Date

### Like

Stores:

- User
- Post
- Created Date

### Comment

Stores:

- User
- Post
- Comment Text
- Created Date

### Follow

Stores:

- Follower
- Following
- Created Date

### Notification

Stores:

- Recipient
- Sender
- Message
- Related Post
- Created Date
- Read Status

---

## 🔐 Authentication

The application provides:

- User Registration
- User Login
- User Logout
- Authentication for creating posts
- Authentication for liking posts
- Authentication for commenting
- Authentication for following users
- User-specific notifications

---

## 📱 Responsive Design

The application is designed to work on:

- Desktop
- Laptop
- Tablet
- Mobile devices

The interface uses responsive CSS to provide a better experience across different screen sizes.

---

## 🧪 Project Testing

The following functionality has been tested:

- User registration
- User login
- User logout
- Profile creation
- Create post
- Image upload
- Like post
- Unlike post
- Comment on post
- Follow user
- Unfollow user
- User search
- Explore page
- Notifications
- Profile page
- Django admin panel

---

## 📌 Project Information

**Project Name:** ConnectHub - Social Media Platform

**Project Type:** Full Stack Development Internship Task

**Backend:** Django

**Database:** SQLite

**Frontend:** HTML, CSS, JavaScript

**Image Handling:** Pillow

**Version Control:** Git & GitHub

---

## 👨‍💻 Author

**Ranjitha Ilapanda**

---

## 📄 License

This project was developed for educational and internship purposes.