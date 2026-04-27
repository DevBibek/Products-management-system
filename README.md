# 📦 Product Management System (Django)

This is a feature-rich **Django-based Product Management System** with authentication, CRUD operations, social login, password reset, object-level access control, and dynamic UI features using JavaScript.

---

## 🚀 About the Project

This project is built using Django framework to learn real-world backend + frontend integration concepts such as authentication, authorization, AJAX-like UI behavior, and secure data handling.

---

## ✨ Features

### 📌 1. CRUD Operations
- ➕ Create products
- 📄 Read product list
- ✏️ Update products
- ❌ Delete products

---

### 📌 2. Authentication System
- 🔐 User Registration (Sign Up)
- 🔑 User Login (Sign In)
- 🚪 User Logout
- 🛡️ Django Authentication system

---

### 📌 3. Social Authentication
- 🔵 Login with Google
- 🐙 Login with GitHub

---

### 📌 4. Password Reset System
- 📧 Forgot password feature
- 🔗 Email link based password reset
- Secure token authentication

---

### 📌 5. Django Messages System
We used `extra_tags` in Django messages framework for better UI feedback:

- ✅ Success messages
- ❌ Error messages
- ℹ️ Info messages

---

### 📌 6. Object-Level Access Control
- Each user can access only their own products
- Prevent unauthorized access
- Secure per-user data handling

---

### 📌 7. JavaScript Dynamic Features ⚡

We used JavaScript for better user experience:

- 🕒 Auto remove messages after 10 seconds
- 🔄 Login/Logout button dynamically changes
  - If user is logged in → shows **Logout**
  - If user is logged out → shows **Login**
- ⚡ Real-time UI update without page refresh

---

## 🛠️ Built With

- Python 🐍
- Django 🌐
- JavaScript ⚡
- SQLite 🗄️
- HTML / CSS 🎨

---

## ⚙️ How It Works

1. User registers or logs in
2. Can login via Google or GitHub
3. Product CRUD operations available
4. Messages appear with auto-hide (10 seconds)
5. UI updates dynamically (Login/Logout button changes)
6. Password reset via email link
7. Object-level access controls data security

---

## 🔐 Security Features

- Django authentication system
- Social login (Google & GitHub)
- Email-based password reset
- Object-level access control

---

## 📥 Installation

```bash
git clone https://github.com/DevBibek/Products-management-system.git
cd Products-management-system
pip install -r requirements.txt
python manage.py runserver