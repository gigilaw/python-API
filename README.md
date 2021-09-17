# Necktie Backend Take-Home Assessment

## Table of Contents

1. [Description](#description)
2. [Set-up Guide](#set-up-guide)
3. [Application Information](#application-information)
4. [Task Answers](#task-answers)

# Description

To build an API server to expose a Doctor List API for front-end
application to present the information to customers.

| Endpoints                     | Description                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------- |
| https://{{domain}}/docter     | To list all doctors and query docters by `district`, `category`, `price range`, and `language` |
| https://{{domain}}/docter/:id | To get a specific doctor by `id`                                                               |

## Requirement

```
- Python 3.6+
```

# Set-Up Guide

## Project Setup

```zsh
# Git clone project
git clone https://github.com/gigilaw/Gigi_Law_Backend_Engineer_Technical_Assessment.git

# Start virtual env
python3 -m venv venv

# Activate env
. venv/bin/activate

# Install required framework and libraries
pip3 install -r requirements.txt

# Set environment variables
export FLASK_APP=app

# Turn on debugger for development environment
export FLASK_ENV=development
```

## Database Setup

```python
# Create sqlite DB
python3
from app import db
db.create_all()

# Seed db with starting data
python3 seed.py
```

## Start application

```zsh
# Start Flask
flask run
```

# Application Information

### Relationship Diagram

![Alt text](https://i.ibb.co/9vdszxy/task.png)

### Database migration

```zsh
# Update migration version
flask db migrate

# Run migration
flask db upgrade
```

### Documentation

TBC

# Task Answers

1. Choice of Framework & Library: Please explain why you choose the particular
   framework or library.
   a. What are the benefits & drawbacks associated with that choice?
   b. What are the assumptions underlying that choice?
2. Potential Improvement: Please elaborate on what kind of improvements you
   would like to implement if you have given more time.
3. Production consideration: Any extra steps should be taken with caution when
   deploying your app to a production environment?
4. Assumptions
   a. Any assumptions you have made when you designed the data model and
   API schema?
   b. Any other assumptions and opinions you have taken throughout the
   assessments?
