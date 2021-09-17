# Necktie Backend Take-Home Assessment

## Description

To build an API server to expose a Doctor List API for front-end
application to present the information to customers.

```
Endpoints:
- https://{{domain}}/docter
- https://{{domain}}/docter/:id
```

###Requirement

```
- Python 3.6+
```

### Set-Up Guide

```zsh
# Git clone project

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

# Start Flask
flask run

```
