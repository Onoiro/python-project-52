[![Actions Status](https://github.com/Onoiro/TaskMan/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Onoiro/TaskMan/actions)
[![Actions Status](https://github.com/Onoiro/TaskMan/actions/workflows/abo-check-task-manager.yml/badge.svg)](https://github.com/Onoiro/TaskMan/actions)
[![Maintainability](https://qlty.sh/badges/8be7044b-186e-41ec-94eb-26e8be04d42b/maintainability.svg)](https://qlty.sh/gh/Onoiro/projects/TaskMan)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3c6f1330d7e0f614ccb3/test_coverage)](https://codeclimate.com/github/Onoiro/TaskMan/test_coverage)

## Welcome to [TaskMan](https://taskman.2-way.ru)
TaskMan is a web application designed to manage tasks in an organization or team. It allows users to register, create, and effectively manage tasks.
The application is deployed and accessible at the following URL: https://taskman.2-way.ru

Key features include:

### Features

- **User Registration**: Users can register to create an account and log in to the TaskMan application.
- **Task Creation**: Users can create tasks with details such as title and description.
- **Assign Task**: Each task can be assigned to a specific user who will be responsible for completing it.
- **Task Status**: Tasks can have various and custom statuses (e.g., To Do, In Progress, Done), making it easy to track progress.
- **Labels**: Tasks can be tagged with labels for better organization and filterability.

### Language Support

The TaskMan application is available in two languages:

- **English**
- **Russian**

### Getting Started with your team

To get started with the TaskMan, follow these steps:
```bash
# clone the repository:
git clone https://github.com/Onoiro/TaskMan.git

# navigate to the project directory:
cd taskman

# create .env file contains environment variables:
touch .env

# open .env file for edit:
nano .env

# specify environment variables in .env, for example:
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
SECRET_KEY="secret_key"
DJANGO_LANGUAGE_CODE="en-us"

# install dependencies, migrate a database, create superuser for admin:
make build

# run app in development mode on local web server:
make dev

# open your browser and navigate to:
http://127.0.0.1:8001/

# run production:
make start

# check code style with flake8:
make lint

# run tests:
make test

# look to the Makefile to find more helpful service commands
```
### Requirements
* OS Linux  
* python = ^3.8.1
* poetry = ^1.2.2
