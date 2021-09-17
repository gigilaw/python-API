# Necktie Backend Take-Home Assessment

## Description

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

## Set-Up Guide

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

# Start Flask
flask run

```
