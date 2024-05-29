# Quick start

## Requirement

* Python < 3.12.0
* For Windows [Install Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

## Configure the project

```bash
python install virtualenv
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

## Setup database (ORM)

```bash
venv\Scripts\activate
flask db init
flask db migrate
flask db upgrade
flask run
```

## Create first business

```bash
venv\Scripts\activate
flask flask create_business
```

## Update requirements

```bash
pip freeze > requirements.txt 
```

## Documentation

* [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/).
* [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/).
* [Flask SqlAlchemy ORM](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/).
* [Fix mysqlclient issue](https://github.com/PyMySQL/mysqlclient).