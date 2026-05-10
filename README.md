# Web Services and Applications Project

![lichens](lichens.jpg)

This is the repository for my Big Project for the Web Services and Applications module of the [Higher Diploma in Science in Computing in Data Analytics at ATU Galway-Mayo](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics). My lecturer is [Andrew Beatty](https://github.com/andrewbeattycourseware?tab=overview&from=2022-12-01&to=2022-12-31).

The focus of this project is to create a web application that uses RESTful APIs to perform CRUD operations on data stored in a database. The application I built is called [**Lichen Tracker**](https://morgam7.pythonanywhere.com/). It allows users to record, view, update, and delete lichen sightings.

## Author

Marcella Morgan

## Hosted Application

The hosted version of this project is available here:

https://morgam7.pythonanywhere.com/


## Project Overview

Lichen Tracker is a Flask web application that allows users to record lichen sightings. A user can select or create a username, post a lichen sighting, view all sightings, update or delete existing records, and browse records by lichen name, location, or user.

The application uses a SQLite database and a RESTful API. The frontend pages use JavaScript `fetch()` requests to communicate with the Flask API routes.

The project was designed to meet the brief by including:

- A Flask web application
- A RESTful API
- CRUD operations
- A SQLite database
- A web interface
- JavaScript `fetch()` calls
- More than one database table
- A hosted version on PythonAnywhere
- Mobile-friendly page layouts

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Fetch API
- Git and GitHub
- PythonAnywhere
- Virtual environment (`venv`)

## Getting Started

To run this project locally, you will need:

1. **Python**  
   I used Python in a virtual environment.

2. **A text editor or IDE**  
   I used [Visual Studio Code](https://code.visualstudio.com/).

3. **The required Python packages**  
   These are listed in `requirements.txt`.

## Local Setup

Clone the repository and move into the project folder.

Create a virtual environment:

`python -m venv venv`

Activate the virtual environment.

On Windows:

`venv\Scripts\activate`

On Mac/Linux:

`source venv/bin/activate`

Install the required packages:

`pip install -r requirements.txt`

Run the Flask application:

`python rest.py`

Open the application in a browser:

`http://127.0.0.1:5000`

## Project Structure

WSAA-Big-Project/

- `rest.py`
- `dao.py`
- `lichen_tracker.db`
- `requirements.txt`
- `README.md`
- `static/`
  - `login.html`
  - `index.html`
  - `view.html`
  - `lichen.html`
  - `lichen_name.html`
  - `location.html`
  - `user.html`
  - `update.html`

## Main Files

### `rest.py`

This file contains the Flask application and the REST API routes. It serves the HTML pages and handles API requests for users and lichen records.

### `dao.py`

This file contains the database access functions. It connects to the SQLite database and contains the SQL queries used to create, read, update, and delete data.

### `lichen_tracker.db`

This is the SQLite database used by the application.

### `requirements.txt`

This file lists the Python packages needed to run the project.

### `static/`

This folder contains the frontend HTML pages. These pages use JavaScript `fetch()` to communicate with the Flask API.

## Database

The project uses a SQLite database called `lichen_tracker.db`.

The database contains two main tables.

### `users`

This table stores usernames.

Example fields:

- `userID`
- `username`

### `lichens`

This table stores lichen sighting records.

Example fields:

- `id`
- `name`
- `comment`
- `location`
- `latitude`
- `longitude`
- `userID`

The `userID` field links each lichen record to the user who posted it.

## API Routes

| Method | Route | Description |
|---|---|---|
| GET | `/users` | Gets all users |
| POST | `/login` | Selects an existing user or creates a new user |
| GET | `/lichens` | Gets all lichen records |
| GET | `/lichens/<id>` | Gets one lichen record by ID |
| POST | `/lichens` | Creates a new lichen record |
| PUT | `/lichens/<id>` | Updates an existing lichen record |
| DELETE | `/lichens/<id>` | Deletes a lichen record |

## Page Routes

| Route | Page |
|---|---|
| `/` | Login / user selection page |
| `/post` | Post a new lichen |
| `/view` | View all lichens |
| `/lichen?id=<id>` | View an individual lichen record |
| `/lichen-name?name=<name>` | View posts by lichen name |
| `/location?location=<location>` | View posts by location |
| `/user?id=<id>` | View posts by user |
| `/update?id=<id>` | Update a lichen record |

## CRUD Functionality

The application demonstrates CRUD operations through the REST API.

### Create

A user can create a new lichen record using the post page. This sends a `POST` request to `/lichens`.

### Read

A user can view all lichen records using `GET /lichens`.

A user can also view an individual lichen record using `GET /lichens/<id>`.

### Update

A user can update an existing lichen record using `PUT /lichens/<id>`.

### Delete

A user can delete a lichen record using `DELETE /lichens/<id>`.

## User Flow

The application starts on a login/user selection page.

A user can select an existing username or create a new one. This is a simple user selection system rather than full secure authentication.

After selecting a user, the user is brought to the post page. When a lichen is posted, the record is stored in the SQLite database and linked to the selected user.

The user can then view all lichen records. From the main view page, the user can:

- View an individual lichen record
- Update a record
- Delete a record
- View all records for a particular lichen name
- View all records from a particular location
- View all records posted by a particular user
- Post another lichen
- Change user

## Features

- Simple user selection/sign-in flow
- Add lichen records
- View all lichen records
- View one lichen record
- Update lichen records
- Delete lichen records
- View records by lichen name
- View records by location
- View records by user
- Records linked to users
- Mobile-friendly layout
- Hosted web application

## Highlights and Challenges

### REST API and CRUD

The main focus of the project was building a RESTful API that could perform CRUD operations. The lichen records can be created, read, updated, and deleted using API routes. The frontend uses JavaScript `fetch()` requests to interact with these routes.

### Database Handling

The project uses SQLite. I separated the database code into a `dao.py` file so that the main Flask routes in `rest.py` would be easier to read and maintain. One practical issue was making sure the database path worked both locally and on PythonAnywhere.

### User-Linked Records

I added a users table so that lichen records could be linked to the user who posted them. This allowed me to add a user profile-style page showing all lichens submitted by a particular user.

### Navigation and Filtering

I added pages to view records by lichen name, location, and user. This means the project goes beyond basic CRUD and allows the user to browse the records in different ways.

### Mobile Layout

I updated the HTML and CSS so that the pages display better on mobile screens. This included adding viewport settings, responsive layouts, and scrollable tables where needed.

### Hosting

The project is hosted on PythonAnywhere. One challenge was making sure the hosted version used the correct files from GitHub and that the SQLite database was in the correct location.

## Limitations

The user selection system is not secure authentication. It is a simple sign-in/user selection flow used to link lichen records to usernames.

The application stores user-submitted lichen records in its own SQLite database. It does not connect to a live external biodiversity database.

The application is intended as a college project to demonstrate Flask, REST APIs, CRUD operations, SQLite, and frontend API calls.

## References

I used the module lecture notes and class materials as a guide when completing this project, along with the course repository:

- [Andrew Beatty WSAA Courseware](https://github.com/andrewbeattycourseware/wsaa-courseware)

I also used the following documentation and references:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [MDN Web Docs — Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [PythonAnywhere Flask Hosting Help](https://help.pythonanywhere.com/pages/Flask/)
- [National Biodiversity Data Centre — Lichens](https://biodiversityireland.ie/taxonomic-groups/lichens/)
- [Biodiversity Maps](https://maps.biodiversityireland.ie/)

## AI Use

I used ChatGPT as an AI support tool while completing this project. All code was reviewed and tested before submission.

