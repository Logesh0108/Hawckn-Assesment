🚀 Mini CRM – Django Web Application

A fully functional Customer Relationship Management (CRM) web application built using Django.  
This project demonstrates real-world backend workflows, MySQL database integration, and API testing using Postman.

==================================================

📌 Project Overview

The Mini CRM application is designed to manage customers, products, and orders efficiently.  
It showcases Django project structure, database connectivity with MySQL, and REST-style API usage.

==================================================

✨ Key Features

• Customer management (Create, Read, Update, Delete)  
• Product management  
• Order management  
• Django Admin Panel  
• MySQL database integration  
• REST-style APIs  
• API testing using Postman  
• Clean and modular project structure  

==================================================

🔄 Application Workflow

1. User sends request from browser or Postman  
2. Django URL dispatcher routes the request  
3. Views handle business logic  
4. Models interact with MySQL database  
5. Data is returned as HTML or JSON response  

Logical Flow:

Browser / Postman → URL → View → Model → MySQL Database → Response

==================================================

🗄️ Database Used

Database Name:
• MySQL

Why MySQL:
• Industry-standard relational database  
• High performance and reliability  
• Scalable for production use  
• Strong support with Django ORM  

Database stores:
• Customer data  
• Product information  
• Order details  

==================================================

📂 Project Structure

mini_crm/
│
├── core/                     Main application logic
│   ├── models.py             MySQL database models
│   ├── views.py              Business logic
│   ├── urls.py               App routing
│   ├── admin.py              Admin configuration
│
├── mini_crm/                 Project settings
│   ├── settings.py           MySQL configuration
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/                HTML templates
├── static/                   Static assets
├── manage.py                 Django entry point
└── requirements.txt          Project dependencies

==================================================

📋 Requirements

Software Requirements:
• Python 3.9 or higher  
• Django 4.x  
• MySQL Server  
• Git  
• Virtual Environment  
• Postman (API testing)  

Python Packages:
Install all dependencies using:
pip install -r requirements.txt

==================================================

⚙️ Installation & Setup

Clone the repository:
git clone https://github.com/Logesh0108/Hawckn-Assesment.git
cd Hawckn-Assesment

Create virtual environment:
python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Configure MySQL in settings.py:
• Database name
• Username
• Password
• Host
• Port

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the server:
python manage.py runserver

Access the application:
http://127.0.0.1:8000/

==================================================

🔐 Admin Panel

Create superuser:
python manage.py createsuperuser

Admin URL:
http://127.0.0.1:8000/admin/

==================================================

📬 API & Postman Usage

The application provides REST-style APIs for core operations.

API Testing Tool:
• Postman

Sample API Endpoints:
• GET    /api/customers/          Fetch all customers  
• POST   /api/customers/          Create new customer  
• PUT    /api/customers/{id}/     Update customer  
• DELETE /api/customers/{id}/     Delete customer  

Postman is used to:
• Send API requests  
• Validate responses  
• Test CRUD operations  
• Verify backend logic  

==================================================

🛠️ Tech Stack

Backend:
• Python
• Django

Frontend:
• HTML
• CSS
• JavaScript

Database:
• MySQL

Tools:
• Git
• GitHub
• Postman

==================================================

🚧 Future Enhancements

• Authentication and role-based access  
• Django REST Framework integration  
• Advanced reporting dashboards  
• Cloud deployment  
• Performance optimization  

==================================================

👨‍💻 Author

Logesh N  
Django Developer | Python Enthusiast  
GitHub: https://github.com/Logesh0108  

==================================================

📄 License

This project is developed for learning, assessment, and demonstration purposes.
