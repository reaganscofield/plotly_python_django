# 4G Capital 
============

Requirements:

1. Python 3.6 
2. pip 19.2.3 or any version 

# Setting Up Project  <br/>

Install virtual environement on your machine

```
 sudo apt install virtualenv
```

Clone repository 

```
    git clone https://scofieldreagan@bitbucket.org/djpbadenhorst/4g_reagan.git
```

Navigate to project root directory 

```
    cd 4g_reagan/project
```

Create virtual enviroment

```
    virtualenv -p python3  virtual_env
```

Activate virtual environment 

```
    source virtual_env/bin/activate
```

Install dependecies

```
    pip install -r requirements.txt
```

Run migartions 

```
    python3 manage.py makemigrations
```

```
    python3 manage.py migrate
```

Run project

```
    python3 manage.py runserver
```

open your google and got to http://127.0.0.1:8000/
