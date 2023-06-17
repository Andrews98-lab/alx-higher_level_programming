# Python - Object-relational Mapping (ORM)

This repository contains code and resources related to the Python - Object-relational Mapping (ORM) project. The purpose of this project is to demonstrate the implementation of ORM concepts in Python for working with relational databases.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Object-relational mapping (ORM) is a technique that allows developers to work with relational databases using object-oriented programming concepts. It provides an abstraction layer that maps database tables to Python classes and allows for seamless interaction between the application and the database.

This project showcases a basic implementation of an ORM in Python. It includes examples of how to define database models as Python classes, perform CRUD (Create, Read, Update, Delete) operations, and execute queries using the ORM.

## Installation

To use this project, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/orm-project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd orm-project
   ```

3. Install the required dependencies. It is recommended to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   pip install -r requirements.txt
   ```

4. Set up the database connection details. Open the `config.py` file and modify the values according to your database configuration.

5. Initialize the database. Run the following command:

   ```bash
   python initialize_database.py
   ```

   This will create the necessary tables in the database.

## Usage

The main components of the ORM implementation can be found in the `orm` directory. The `models.py` file contains the model definitions, where each model represents a database table. You can define new models or modify existing ones to fit your application's needs.

To perform CRUD operations or execute queries, you can use the `orm.py` module. This module provides methods for creating, retrieving, updating, and deleting records, as well as executing custom SQL queries.

For example, to create a new record:

```python
from orm import ORM

# Instantiate the ORM
orm = ORM()

# Create a new record
new_user = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'age': 25
}
orm.create('users', **new_user)
```

More usage examples and documentation can be found in the code comments and the provided examples.


