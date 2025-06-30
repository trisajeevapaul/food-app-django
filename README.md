
# Little Lemon Restaurant Web App 🍋

This is a Django-based full-stack web application developed as part of a portfolio project. The application simulates a restaurant management system for **Little Lemon**, featuring menu display, order handling, and booking functionalities.

## 🔧 Tech Stack

- **Backend**: Python, Django
- **Database**: SQLite
- **Frontend**: HTML, Django Templates
- **Admin Interface**: Django Admin

## 📁 Project Structure

```
├── app/
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── forms.py          # Booking and Order forms
│   ├── models.py         # MenuItem, Order, OrderItem models
│   ├── urls.py           # URL routing
│   ├── views.py          # View logic
│   └── migrations/       # Database schema migrations
├── db.sqlite3            # SQLite database file
├── manage.py             # Django management script
```

## 🚀 Features

- 🧾 **Menu Management**: View menu items with image, name, description, and price.
- 🛒 **Online Orders**: Place and manage orders via form submissions.
- 📆 **Table Booking**: Book a table with date and time.
- 🔐 **Authentication**: Secure login/logout for admin and users.
- ⚙️ **Admin Panel**: Manage menu, orders, and users using Django Admin.

## 📸 Screenshots

(Include screenshots of menu page, booking form, order form, and admin panel)

## ✅ Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/little-lemon-restaurant.git
   cd little-lemon-restaurant
   ```

2. **Set up virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   Open `http://127.0.0.1:8000/` in your browser.

## 🧪 Superuser Access (for Admin)

Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

Then visit: `http://127.0.0.1:8000/admin/`

## 📂 Media & Static Files

- Media folder is used for uploading menu images.
- Configure `MEDIA_URL` and `MEDIA_ROOT` in `settings.py` to serve media properly.

## 🙌 Credits

Developed by Trisa Jeevapaul as part of a Django learning project.
