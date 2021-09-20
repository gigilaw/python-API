# Necktie Backend Take-Home Assessment

## Table of Contents

1. [Description](#description)
2. [Set-up Guide](#set-up-guide)
3. [Application Information](#application-information)
    - [Database Relationship Diagram](#relationship-diagram)
    - [Database Migration Commands](#database-migration)
    - [API Documentation](#documentation)
    - [Application Testing](#application-testing)
4. [Task Answers](#task-answers)

# Description

To build an API server to expose a Doctor List API for front-end
application to present the information to customers.

| Endpoints                     | Description                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------- |
| https://{{domain}}/doctor     | To list all doctors and query doctors by `district`, `category`, `price range`, and `language` |
| https://{{domain}}/doctor/:id | To get a specific doctor by `id`                                                               |

## Python Version

```
Python 3.9.7
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

## Relationship Diagram

![Alt text](./storage/db.png)

## Database migration

```zsh
# Update migration version
flask db migrate

# Run migration
flask db upgrade
```

## Documentation

### GET /doctor

```http
GET /doctor
```

| Query Parameters | Description                                      |
| :--------------- | :----------------------------------------------- |
| `categoryId`     | **optional**.                                    |
| `districtId`     | **optional**.                                    |
| `languageId`     | **optional**.                                    |
| `gt`             | **Requried for price_range query**. Greater than |
| `lt`             | **Requried for price_range query**. Less than    |

### Sample Success Response

```json
[
	{
		"category": {
			"id": 3,
			"name": "Cardiologist"
		},
		"clinic": {
			"address": "48290 Ross Corners Apt. 605\nChristopherberg, MT 71616",
			"contact": "761-697-4127x9538",
			"district": {
				"id": 1,
				"name": "Wan Chai"
			},
			"hours": "Monday: 9am-8pm, Friday: 9am-8pm, Saturday: closed, Sunday: closed, Public Holiday: closed",
			"include_medications": false,
			"medication_days": null,
			"name": "Moon Ltd Clinic",
			"price": 430
		},
		"first_name": "Luis",
		"last_name": "Medina",
		"id": 1
	},
	{
		"category": {
			"id": 3,
			"name": "Cardiologist"
		},
		"clinic": {
			"address": "Unit 5772 Box 0035\nDPO AP 77801",
			"contact": "0807345494",
			"district": {
				"id": 1,
				"name": "Wan Chai"
			},
			"hours": "Monday: 9am-8pm, Friday: 9am-8pm, Saturday: closed, Sunday: closed, Public Holiday: closed",
			"include_medications": false,
			"medication_days": null,
			"name": "Moreno, Hernandez and Beard Clinic",
			"price": 450
		},
		"first_name": "Brandon",
		"last_name": "Schneider",
		"id": 2
	}
]
```

### GET /doctor/:id

```http
GET /doctor/:id
```

| Query Parameter | Type      | Description                |
| :-------------- | :-------- | :------------------------- |
| `id`            | `integer` | **Required**. Id of doctor |

### Sample Success Response

```json
{
	"category": {
		"id": 1,
		"name": "General Practitioner"
	},
	"clinic": {
		"address": "3752 Vega Square\nTimothyport, NM 80530",
		"contact": "581-201-2681x011",
		"district": {
			"id": 1,
			"name": "Wan Chai"
		},
		"hours": "Monday: 9am-3pm, Tuesday: 9am-3pm, Wednesday: 9am-3pm, Thursday: 9am-3pm",
		"include_medications": true,
		"medication_days": 5,
		"name": "Klein Inc Clinic",
		"price": 840
	},
	"first_name": "Andy",
	"last_name": "April",
	"id": 1
}
```

### POST /doctor

```http
POST /doctor
```

| Parameters   | Type      | Description             |
| :----------- | :-------- | :---------------------- |
| `firstName`  | `string`  | **Required**.           |
| `lastName`   | `string`  | **Required**.           |
| `gender`     | `string`  | **Required**.           |
| `categoryId` | `integer` | **Required**.           |
| `clinicId`   | `integer` | **Required**.           |
| `languages`  | `array`   | **Required**. Ex. [1,2] |

### Sample Success Response

```json
{
	"category": {
		"id": 1,
		"name": "General Practitioner"
	},
	"clinic": {
		"address": "230 Regina Plaza Apt. 591\nScottberg, WA 83789",
		"contact": "893.679.6237",
		"district": {
			"id": 1,
			"name": "Wan Chai"
		},
		"hours": "Monday: 9am-8pm, Friday: 9am-8pm, Saturday: closed, Sunday: closed, Public Holiday: closed",
		"include_medications": false,
		"medication_days": null,
		"name": "Lowe and Sons Clinic",
		"price": 940
	},
	"first_name": "333",
	"last_name": "def",
	"id": 1
}
```

## Application Testing

```zsh
# Run tests
python3 test.py
```

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
