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