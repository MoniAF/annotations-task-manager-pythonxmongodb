# Annotations — Task Management Application

A simple task management web application developed as an independent learning project during my university break in July 2024. The main goal was to explore Python web development and gain practical experience working with MongoDB.

The application allows users to create, view, update, and delete tasks through a web interface, storing task information in a MongoDB database.

## Technologies

- **Language:** Python
- **Web Framework:** Flask
- **Database:** MongoDB
- **Database Driver:** PyMongo
- **Frontend:** HTML5, CSS3
- **Templating Engine:** Jinja2

## Features

- **Create Tasks:** Register tasks with a date, name, description, and priority level.
- **View Tasks:** Display all saved tasks in a table.
- **Update Tasks:** Edit existing task information.
- **Delete Tasks:** Remove tasks from the database.
- **Priority Management:** Assign High, Medium, or Low priority levels to tasks.
- **Database Integration:** Store and manage task records using MongoDB and PyMongo.

## Project Structure

```text
Annotations/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── css/
│       └── styles.css
│
└── templates/
    ├── index.html
    ├── tasks.html
    └── updatetask.html
```

## Installation and Setup

Follow these steps to run the application locally on Windows.

### 1. Check Python Installation

Open PowerShell and verify whether Python is installed:

```powershell
py --version
```

If Python is not installed, download it from the [official Python website](https://www.python.org/downloads/).

This project was tested using Python 3.14.4.

### 2. Create a Virtual Environment

Open a terminal in the project directory and create a virtual environment:

```powershell
py -3.14 -m venv .venv
```

### 3. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

Once activated, `(.venv)` should appear at the beginning of the terminal prompt.

### 4. Install Dependencies

Install the required Python packages using the requirements file:

```powershell
python -m pip install -r requirements.txt
```

### 5. Install and Configure MongoDB

MongoDB Community Server must be installed on your computer.

Download it from the official website:

[MongoDB Community Server](https://www.mongodb.com/try/download/community)

During installation, select the **Complete** setup type and enable **Install MongoD as a Service** to configure MongoDB as a Windows service.

### 6. Check MongoDB Service Status

After installation, open PowerShell and execute:

```powershell
Get-Service MongoDB
```

The expected status is:

```text
Status    Name
------    ----
Running   MongoDB
```

### 7. Start MongoDB if Necessary

If the service status is `Stopped`, execute:

```powershell
Start-Service MongoDB
```

Check the service status again to confirm that it is running.

### 8. Run the Application

Return to the project directory, make sure the virtual environment is active, and execute:

```powershell
python app.py
```

Flask will start the local development server.

### 9. Open the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

The task management application should now be available.

## Database Configuration

The application connects to MongoDB through the following local connection:

```python
client = MongoClient('mongodb://localhost:27017/')
```

It uses the following database and collection:

- **Database:** `AnnotationsDB`
- **Collection:** `tasks`

MongoDB automatically creates the database and collection when the first task document is inserted, provided they do not already exist.

Each task is stored as a document containing the following fields:

- `datetask`: Task date.
- `name`: Task name.
- `description`: Task description.
- `priority`: Task priority level.

## Learning Objectives

This project provided an opportunity to:

- Explore Python web development using Flask.
- Understand how to connect a web application to MongoDB using PyMongo.
- Implement CRUD operations with a NoSQL database.
- Work with MongoDB documents and ObjectId-based identification.
- Practice handling HTML forms and dynamic templates using Jinja2.

## Project Information

- **Project Type:** Independent Learning Project
- **Development Period:** July 2024
- **Focus Areas:** Python, Web Development, and NoSQL Database Integration.