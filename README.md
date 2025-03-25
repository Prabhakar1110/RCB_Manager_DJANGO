SDLC Document for "RCB_CRUD_DJANGO" Project:
------------------------------------------
1. Project Overview:
-------------------
    Project Name: RCB_CRUD_DJANGO
    Technologies Used: 
    Frontend: HTML, CSS, Bootstrap5, JS, DTL
    Backend: Django Framework
    DB: SQLite3 (PostgreSQL in Prod)

2. SDLC Phases:
--------------
2.1 Planning:
    Objective: Create, Read, Update, and Delete (CRUD) operations for RCB team.

2.2 Requirement Analysis:
    Functional Requirements: 
        1.User can add, update, delete, and view player details.
        2.Profile picture upload functionality.
    Non-Functional Requirements:
        1.Responsive UI using Bootstrap5.
        2.Secure data handling(csrf token).
        3.Scalability for future enhancements.

2.3 Design:
    System Architecture:
        Frontend: HTML, CSS, Bootstrap, JS, Django Template Language (DTL)
        Backend: Django (MVT pattern)
        Database: SQLite3 (PostgreSQL in Prod)
    Database Design (Players Model) - Fields and DataTypes:
        | Field Name    | Data Type     |
        |---------------|---------------|
        | name          | CharField(100)|
        | age           | IntegerField  |
        | role          | CharField(100) - dropdown|
        | country       | CharField(50) - dropdown|
        | profile_pic   | ImageField    |
        | is_captain    | BooleanField - single checkbox |
        | fav_food      | BooleanField - Checkboxes |

2.4 Development:
    Setup Django Projects & Apps:
        1.Create and activate Virtual environment: py -m venv rcb_venv
        2.Install Django while Virtual environment is active
        3.Create Project: django-admin startproject RCB_CRUD_DJANGO
        4.cd RCB_CRUD_DJANGO
        5.To run: python manage.py runserver
        6.To create App: py manage.py startapp crud
        7.Define Models: (As per the table above)
        8.Migrate Database:
            1.python manage.py makemigrations
            2.python manage.py migrate

    Create Views & Templates: Implement CRUD functionality with Django views and templates.
    Apply Bootstrap for UI Styling.

3. Conclusion:
    The RCB CRUD Application is a full-stack Django project that manages player details effectively using a structured SDLC approach. This document serves as a roadmap for development.
