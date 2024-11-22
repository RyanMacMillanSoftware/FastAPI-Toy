# FastAPI-Toy
Trying out Python FastAPI.

## The task
Build the following APIs.

### GET /wines
Response:
```json
200 OK
{
    "wines": [
        {
            "id": 1,
            "name": "Cab Sav"
        },
    ]
}
```

### POST /wines

Request:
```json
{
    "name": "Savvy B"
}
```

Response:
```json
201 Created
```

## Project setup
### Setup env and install dependencies
1. Clone the project
2. cd into the project directory
3. Create a virtual env to work in and install the requirements

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### Run the API
From the console inside the venv where fastapi will be installed
```bash
fastapi dev main.py
```