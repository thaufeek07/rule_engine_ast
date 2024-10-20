# Rule Engine with AST

## Description

This project implements a simple 3-tier rule engine application that uses an Abstract Syntax Tree (AST) to represent, combine, and evaluate user-defined rules based on attributes like age, department, salary, and more. The project includes:

A Frontend (UI): A simple web interface for interacting with the rule engine.
An API (Flask): A RESTful API that allows users to create, combine, and evaluate rules.
A Backend: An AST-based rule engine for processing and evaluating user rules.
A Data Layer: SQLite database for storing rules and metadata.
The system is designed to allow dynamic creation, modification, and combination of rules. It also supports user-defined functions for more complex rule logic.

## Features

Dynamic Rule Creation: Allows users to create, combine, and modify rules.
User-Defined Functions: Supports advanced rule logic through custom functions.
Rule Evaluation: Evaluates user rules against input data to determine eligibility.
REST API: Provides endpoints for creating, combining, and evaluating rules via API.
Data Persistence: Stores rules and metadata in an SQLite database.
Frontend UI: A simple HTML form for rule creation and evaluation.

## Project Structure

rule_engine_ast/
│
├── api/                      # Flask API layer
│   └── app.py                # API endpoints and server logic
│
├── engine/                   # Backend logic
│   ├── __init__.py           # Init for backend package
│   ├── ast_engine.py         # Rule engine logic with AST
│   └── db.py                 # SQLite database logic
│
├── templates/                # Frontend UI
│   └── index.html            # HTML form for rule creation and evaluation
│
├── tests/                    # Unit tests for the rule engine
│   └── test_ast_engine.py    # Test cases for the AST and rule evaluation
│
├── venv/                     # Virtual environment (not pushed to GitHub)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore                # Git ignore file
└── main.py                   # Entry point to run the server

## Requirements

The application runs in a Python environment. The dependencies are listed in the requirements.txt file and can be installed using pip.

Python 3.x
Flask (for the API layer)
SQLite (for database storage)

## Running the Application

## Clone the Repository:

git clone https://github.com/your-username/rule-engine-ast.git
cd rule-engine-ast

## Set Up Virtual Environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

## Install Dependencies:

pip install -r requirements.txt

## Initialize the Database:

python -c "from engine.db import create_rule_table; create_rule_table()"

## Run the Application:

python api/app.py
