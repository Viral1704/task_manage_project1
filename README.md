##🎯 Task Manager REST API – Flask
#📌 Overview

A secure backend REST API built with Flask that allows users to manage their tasks efficiently.
The system enforces authentication and ownership-based access control to ensure data privacy.

#🏗 Architecture

RESTful API design

Token-based authentication

ORM-based database management

Modular project structure

#🎯 Objective

To develop a production-ready backend service that:

Authenticates users securely

Allows users to manage personal tasks

Prevents unauthorized access

Follows real-world API standards

#🛠 Tech Stack

Python

Flask

Flask-SQLAlchemy (ORM)

SQLite

Postman (Testing)

#🚀 Key Features

✔ User Registration & Login
✔ Token-based Authentication
✔ Task CRUD Operations
✔ Task Status Tracking
✔ Ownership Validation
✔ Secure API Routes
✔ Error Handling
✔ Clean Code Structure

#🔐 Authentication Flow

User logs in

Server generates token

Token sent in headers

Token validated on every request

#📌 API Endpoints
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Login
POST	/tasks	Create task
GET	/tasks	Fetch user tasks
GET	/tasks/<id>	Get single task
PUT	/tasks/<id>	Update task
DELETE	/tasks/<id>	Delete task
⚙ Setup Guide
Clone Repository
git clone <repo_url>
cd task_manager_api

Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run Server
flask run


Server runs at:

http://127.0.0.1:5000

#🧪 Testing

Tested all APIs using Postman

Verified:

Token validation

Unauthorized access prevention

CRUD functionality

Error responses

#📚 What I Learned

Flask backend architecture

Authentication handling

ORM database management

REST API design

Secure user access

Debugging backend systems

#📈 Project Outcome

Built real-world backend APIs

Improved API security knowledge

Learned scalable backend design

#🏁 Conclusion

This project strengthened my understanding of:

Backend development

API security

Database integration

Real production patterns

⭐ Feel free to star this repo if you found it useful!
