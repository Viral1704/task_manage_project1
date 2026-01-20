✅ Task Manager REST API (Flask)
📌 About the Project

This is a backend REST API built using Flask that allows users to manage their tasks securely.
Each user can create, view, update, and delete only their own tasks using token-based authentication.

This project focuses on real-world backend practices like authentication, authorization, and clean API design.

🎯 Project Objective

Build a secure backend system

Implement authentication using tokens

Enforce user-based data access

Practice real REST API development

🛠 Tech Stack

Python

Flask

Flask-SQLAlchemy

SQLite

Postman (API Testing)

🚀 Features

✔ User registration & login
✔ Token-based authentication
✔ Task CRUD operations
✔ Task status management
✔ Ownership-based access control
✔ Error handling
✔ Clean project structure

🔐 Authentication Flow

User logs in

Server generates a token

Token is sent in request headers

Every request is verified

📌 API Endpoints
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Login user
POST	/tasks	Create task
GET	/tasks	Get all user tasks
GET	/tasks/<id>	Get single task
PUT	/tasks/<id>	Update task
DELETE	/tasks/<id>	Delete task
⚙ Setup Instructions
1. Clone Repository
git clone https://github.com/Viral1704/task_manage_project1.git
cd task_manage_project1

2. Create Virtual Environment
python -m venv task_manage
task_manage\Scripts\activate

3. Install Dependencies
pip install 

4. Run Server
flask run


Server will start at:

http://127.0.0.1:5000

🧪 Testing

All APIs tested using Postman
Verified:

Authentication

Access control

CRUD operations

Error responses

📚 What I Learned

Flask backend architecture

Token authentication

ORM database handling

REST API standards

Debugging production errors

🏁 Conclusion

This project helped me understand real backend development workflow and security practices.

⭐ Author

Viral Vaghasiya
Backend Developer (Flask)
