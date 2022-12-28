ALURA FLIX
============

REST API to deal with System Flow

Requirements
------------

This project requires:

    * Python 3.10 or higher
    * Poetry 1.3.1 or higher to deal with dependencies

Instalation
------------

```
# Start the enviroment
$ poetry shell

# Install the dependencies (do not install with dev dependencies in production)
$ poetry install --no-dev
```

In the `settings.py` set the `DEBUG` to `False`
```
... all the code before

    DEBUG = False

... all the code after
```

```
# Migrate the tables
$ python3 manage.py migrate

# Start the server
$ python3 manage.py runserver
```

### That's all