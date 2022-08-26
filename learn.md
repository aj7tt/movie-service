
'''
##Overview

Database - connects to the database
Models - describes the data model(s)
CRUD - contains the Create, Read, Update and Delete actions which execute queries on the models against the database
Schemas - defines the schemas of the inputs and outputs of the API
Routers - explains the different routes of the API and what CRUD action to call
Main - instantiates the FastAPI application and adds the routes from the routers


'''





```
.
.
├── app                         # "app" is a Python package
│   ├── __init__.py             # this file makes "app" a "Python package"
│   ├── main.py                 # "main" module, e.g. import app.main
│   ├── dependencies.py         # "dependencies" module, e.g. import app.dependencies
│   └── api                     # "api" is a "Python subpackage"
│   │   ├── __init__.py         # makes "api" a "Python subpackage"
│   │   ├── items.py            # "items" submodule, e.g. import app.api.items
│   │   └── users.py            # "users" submodule, e.g. import app.api.users
│   └── internal                # "internal" is a "Python subpackage"
│       ├── __init__.py         # makes "internal" a "Python subpackage"
│       └── admin.py            # "admin" submodule, e.g. import app.api.admin
|── env
|── gitignore
|──requirements.txt

```