# FastAPI-Toy
Trying out Python FastAPI.
The aim is to build from the ground up with FastAPI, SQLAlchemy, and Pydantic. Intentially avoiding any templates or tools to speed up project setup so I can focus on the basics of spinning up a new API with the necessary tooling.

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

### Next steps
Once the API is working as intended move on to these improvements:
- Add limit and offset to the GET API
- Containerise, use docker and docker compose
- Move from SQLite to Postgres in docker
- Enhance the generated docs

### Won't do
Testing. Quality isn't the purpose of this project. 

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