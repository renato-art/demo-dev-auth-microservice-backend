<div align="center">
    <h1>Auth system</h1>
    <h4>Auth system microservice backend demonstration using factory pattern<h4>
    ![zarak-khan-Ve2SL0zMhWk-unsplash](https://raw.githubusercontent.com/andela-mnzomo/project-dream-team-one/master/flask-crud-part-one.jpg)
</div>

## Architecture

Directory tree based on the factory design pattern, used to serve multiple packages with a MVC structure.

```
.
├── app
│   ├── exceptions
│   │   └── users_exceptions.py
│   ├── models
│   │   └── user_model.py
│   ├── tests
│   │   └── features
│   │       ├── steps
│   │       │   ├── delete_users.py
│   │       │   └── get_users.py
│   │       ├── delete_users.feature
│   │       ├── environment.py
│   │       └── get_users.feature
│   ├── views
│   │   ├── __init__.py
│   │   └── home_view.py
│   └── __init__.py
├── .env
├── .gitignore
├── requirements.txt
└── schema.sql

7 directories, 14 files
```

## Setup

* Clone the repository & `cd` to the root directory.

* Create a virtual environment with the command:

```
python -m venv venv
```

* Execute the command below to install the dependencies of the project:

```
pip install -r requirements.txt
```

## Run

Enter in the virtual environment with the command:

```
source venv/bin/activate
```

Run the flask application with the command:

```
flask run
```

The application will run locally in port `5000`.

## API Routes

This is a CRUD application, that manipulates a Postgres database using the psycopg2 library.

### CREATE Route

* The create route can be accessed using a POST request in the `/users` link.

* To make this request you need to send a JSON file in the body of the requisition, with the values `name, email and password`.

Requisition example:

```
{
    "name": "test",
    "email": "test@mail.com",
    "password": "1234abcd"
}
```

* This request will return the object in a JSON format and the HTTP status code 201.

### READ Route

* The read route can be accessed using a GET request in the `/users` link.

* This request will return a list of the users presents in the database, with the HTTP status code 200.

* The id returned in the request is created automatically when you save a user into the database.

Return example:

```
[
    {
        "email": "test@mail.com",
        "id": "40e6215d-b5c6-4896-987c-f30f3678f608",
        "name": "test",
        "password": "1234abcd"
    },
    {
        "email": "example@mail.com",
        "id": "6ecd8c99-4036-403d-bf84-cf8400f67836",
        "name": "example",
        "password": "1234abcd"
    }
]
```

### UPDATE Route

* Not implemented yet.

### DELETE Route

* The delete route can be accessed using a DELETE request in the `/users/id` link, passing as the `id` argument an integer number.

* This request will return nothing, with the HTTP status code 204.

## Run the tests

* This application uses the Behavior Driven Development to do the tests, sou you need to run the code below to perform them:

```
behave app/tests/features
```

## Remarks

This template is developed and tested on

- Python 3.9
- Ubuntu 20.04.3 LTS
