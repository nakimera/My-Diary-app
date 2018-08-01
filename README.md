# My-Diary-app
My Diary is an online journal where users can pen down their thoughts and feelings. 

## Getting started

### Prerequisites
You will need the following software running on your machine to get started

* Python 3.6
is an intepreted high-level programming language that was used for this application

* pip
is a package management system used to install and manage software packages written in python

* Postgres database

### Technologies used
* Flask
* Pytest
* Pylint

Download python from [here](https://www.python.org/getit/)
Download pip from [here](https://pip.pypa.io/en/stable/reference/pip_download/)
Download Postgres database software from [here]( https://www.postgresql.org/download/)

### Setting up the application
These are the steps on how to get a development environment of the application running on your machine

 - cd to where you want to create your repository

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

Run the development server
```
$ python run.py
```

### Setting up the database
Install postgres database on your machine

The app should now be running on http://localhost:5000

The following endpoints can be tested

| METHOD       | Endpoint           | Functionality  |
| ------------- |:-------------:| -----|
| POST     | /api/v1/auth/signup | Register a user |
| POST     | /api/v1/auth/login   | Login a user    |
| GET      | /api/v1/entries | Get all entries for a user    |
| GET      | /api/v1/entries/id      | Fetch the details of an entry for a user |
| POST | /api/v1/entries      | Add an entry |
| PUT      | /api/v1/entries/id      | Modify an entry|

### How to run tests
- Install pytest 
```
$ pip install pytest
```
 - Run tests
 ```
$ cd ~/my-diary-app/tests
$ pytest test_entry.py
 ```

## Deployment  sites
The user interfaces are hosted on github pages at https://nakimera.github.io/My-Diary/

The api is hosted on heroku at 