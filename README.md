# Quick start

## Configure the project

```bash
python install virtualenv
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

## Configure the ORM database

```bash
venv\Scripts\activate
flask db init
flask db migrate
flask db upgrade
flask run
```

## Create first user

```bash
venv\Scripts\activate
flask create-user-admin
```

## Update requirements

```bash
pip3 freeze > requirements.txt 
```

## Documentation

* [Fix mysqlclient issue](https://github.com/PyMySQL/mysqlclient).