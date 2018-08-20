[![Build Status](https://travis-ci.org/nakimera/My-Diary-app.svg?branch=feature-api-endpoints)](https://travis-ci.org/nakimera/My-Diary-app)
[![Coverage Status](https://coveralls.io/repos/github/nakimera/My-Diary-app/badge.svg?branch=feature-api-endpoints)](https://coveralls.io/github/nakimera/My-Diary-app?branch=feature-api-endpoints)

# My-Diary-app
My Diary is an online journal where users can pen down their thoughts and feelings. 

## Getting started

### Prerequisites
You will need the following software running on your machine to get started

* Python 3.6 (Intepreted high-level programming language that was used for this application)

* pip (Package management system used to install and manage software packages written in python)

* Postgres database (Open source relational database management system )

### Technologies used
* Flask (Python framework)
* Pytest (Python testing framework)
* Pylint (Bug and quality checker for the Python programming language)

[Download python](https://www.python.org/getit/)

[Download pip](https://pip.pypa.io/en/stable/reference/pip_download/)

[Download Postgres database software]( https://www.postgresql.org/download/)

### Setting up the application
These are the steps on how to get the application running on your machine

 - In your terminal, cd to where you want to create your repository

- Clone the project repo
```
$ git clone https://github.com/nakimera/My-Diary-app.git
```

- Install a virtual environment via pip
``` 
$ pip install virtualenv 
```

- Create a virtual environment
```
$ virtualenv env
```
Where env is the environment name. You can change it to your preferance.

- Activate the virtual environment
```
$ my-diary-app/env/scripts/activate
```

Install requirements
```
pip install -r requirements.txt
```

### Setting up environment variables for the development and testing environments
- On windows, search for Edit environment variables

- Under user variables, select New

- Add the following environment variables using the respective variable name & variable value pairs

| Variable name         | Variable value         | 
| ----------------------|:-------------------------------------------------------:| 
| APP_ENV               | None                                  |                                       
| DATABASE_URL          | postgresql://user:password@localhost/database_name      |
| TEST_DATABASE_URL     | postgresql://user:password@localhost/test_database_name |

### Running the development server

- Set APP_ENV value to development

- Run the app with the command below

```
$ python run.py
```

The app should now be running on http://localhost:5000

The following endpoints can be tested using postman

| METHOD       | Endpoint           | Functionality  |
| ------------- |:-------------:| -----|
| POST     | /api/v1/auth/signup | Register a user |
| POST     | /api/v1/auth/login   | Login a user    |
| GET      | /api/v1/entries | Get all entries for a user    |
| GET      | /api/v1/entries/id      | Fetch the details of an entry for a user |
| POST | /api/v1/entries      | Add an entry |
| PUT      | /api/v1/entries/id      | Modify an entry|

### Running tests
- Set APP_ENV value to testing

- Open a new terminal and cd to the tests folder

 ```
$ cd ~/my-diary-app/tests
$ pytest 
 ```

 - Running tests with coverage
 ```
 $ pytest --cov
 ```

## Deployment  sites
[User interfaces](https://nakimera.github.io/My-Diary/)

[Heroku](https://my-diary-app-np.herokuapp.com) 

[Api Documentation](https://mydiaryapp.docs.apiary.io/#)