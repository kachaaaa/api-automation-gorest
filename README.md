# API Automation Project — GoRest

## Description
This is a learning project for practicing API automation using Python, Requests, and Pytest.
It includes:
- GET test to retrieve the list of users
- POST test to create a new user
- Token management via `.env` file

## Project Structure

api-automation-gorest/
├── .gitignore
├── pytest.ini
├── requirements.txt
├── README.md
├── tests/
│   └── test_users.py
└── utils/
├── init.py
└── config.py

## Installation & Usage
1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

2. Install dependencies:
pip install -r requirements.txt

3. Create a .env file in the project root and add your token:
GOREST_TOKEN=your_token_here

4. Run tests:
pytest

Features 

 All tokens and secrets are stored in .env (not commited to the repository)

 .giignore is configured for Python and API projects

 Easy to run and extend with additional API tests
