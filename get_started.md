## create virtualenv

```
pip install virtualenv

virtualenv --version

python -m venv env  
            
env\Scripts\activate 

 ```

```
git init

```



## create .gitignore file

```
__pycache__
.env
env
test_db.db

```

## create a folder "app and a file inside it  requirements.txt

run 
```
pip install -r requirements.txt

uvicorn
fastapi

```

 pip install --upgrade pip

## inside app name crete a folder confiig and create a file config.py

We will store our project settings and configurations inside of this file named config.py.


#runnn
uvicorn app.main:app --reload 