# 0x03. User Authentication Service

## Project Overview

This project focuses on building a simple user authentication system from scratch using Flask and SQLAlchemy. While such systems are generally implemented using established frameworks (e.g., Flask-User), this exercise is designed to help learners understand the underlying mechanisms of user authentication by implementing each component manually.

## Project Details

- **Track:** Back-end
- **Theme:** Authentication
- **Weight:** 1
- **Start Date:** June 1, 2025, 6:00 PM  
- **End Date:** June 5, 2025, 6:00 PM  
- **Checker Release:** June 2, 2025, 6:00 PM  
- **Auto Review Launch:** At project deadline

## Learning Objectives

By the end of this project, you should be able to:

- Declare API routes in a Flask app
- Get and set cookies in Flask
- Retrieve form data from requests
- Return appropriate HTTP status codes

## Requirements

- **Editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 18.04 LTS
- **Python Version:** 3.7
- **Style Guide:** `pycodestyle` 2.5
- **ORM:** SQLAlchemy 1.3.x
- All Python files must:
  - End with a new line
  - Start with `#!/usr/bin/env python3`
  - Be executable
  - Be documented at module, class, and method/function level
  - Include type annotations
- Flask app must interact **only** with `Auth` class, never directly with the DB
- Only public methods of `Auth` and `DB` classes should be used externally

## Setup

Install required dependency:

```bash
pip3 install bcrypt

Author: Dzeble Kwame Baku
