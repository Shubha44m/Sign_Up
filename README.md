# Django Authentication Project

A beautiful, responsive authentication system built with Django and Tailwind CSS.

## Features

- **User Authentication**: Secure Login and Signup functionality.
- **Responsive Design**: Fully responsive UI that works seamlessly across desktop, tablet, and mobile devices.
- **Modern Aesthetics**: Premium dark-mode UI with glassmorphism effects, powered by Tailwind CSS.
- **User Dashboard**: A personalized dashboard for logged-in users.
- **Form Validation**: Built-in Django form validation with custom error handling and UI alerts.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Tailwind CSS (via CDN)
- **Icons**: Google Material Symbols
- **Database**: SQLite (default for development)

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shubha44m/Sign_Up.git
   cd Sign_Up
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

- `accounts/`: The Django app managing authentication logic (views, forms, urls).
- `auth_project/`: The core Django project configuration.
- `templates/`: Contains all the HTML templates (`base.html`, `login.html`, `signup.html`, `home.html`).
