# 0x00. Personal Data

## 📁 Project Overview

This project focuses on the secure handling of **Personally Identifiable Information (PII)** in backend systems. It addresses logging, filtering sensitive data, secure database connections, and log formatting using Python. It is part of the ALX Software Engineering curriculum under the **Authentication** and **Backend** track.

## 🗓️ Timeline

- **Project start:** May 20, 2025, 6:00 PM  
- **Project deadline:** May 22, 2025, 6:00 PM  
- **Checker release:** May 21, 2025, 6:00 AM  
- **Manual QA review:** Required upon completion  
- **Auto review:** Will launch at deadline  

## 📚 Resources

- [What Is PII, non-PII, and Personal Data?](https://en.wikipedia.org/wiki/Personal_data)
- [Python logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://pypi.org/project/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://realpython.com/python-logging/)

## 🎯 Learning Objectives

By the end of this project, you should be able to:

- Identify PII fields in user data.
- Obfuscate sensitive data using regex in logs.
- Use `bcrypt` for password hashing and validation.
- Authenticate securely to a MySQL database using environment variables.
- Create structured logs with custom formatters.

## ✅ Requirements

- OS: Ubuntu 18.04 LTS
- Python version: 3.7
- Style guide: `pycodestyle` 2.5
- All Python scripts must be executable
- Each file must end with a new line
- Shebang must be: `#!/usr/bin/env python3`
- All modules, classes, and functions must be fully documented
- Type annotations required for all functions

## 🧪 Project Tasks

### 0. Regex-ing

- **Function:** `filter_datum`
- **Purpose:** Obfuscate PII fields in a log line using `re.sub`
- **File:** `filtered_logger.py`

### 1. Log Formatter

- **Class:** `RedactingFormatter`
- **Purpose:** Subclass `logging.Formatter` to redact sensitive fields
- **File:** `filtered_logger.py`

### 2. Create Logger

- **Function:** `get_logger`
- **Purpose:** Return a custom logger named `user_data` with redacting formatter
- **Constants:** `PII_FIELDS` (tuple of 5 key PII fields)
- **File:** `filtered_logger.py`

### 3. Connect to Secure Database

- **Function:** `get_db`
- **Purpose:** Securely connect to a MySQL database using credentials from environment variables
- **Environment Variables:**
  - `PERSONAL_DATA_DB_USERNAME` (default: `root`)
  - `PERSONAL_DATA_DB_PASSWORD` (default: `""`)
  - `PERSONAL_DATA_DB_HOST` (default: `localhost`)
  - `PERSONAL_DATA_DB_NAME`
- **File:** `filtered_logger.py`

### 4. Read and Filter Data

- **Function:** `main`
- **Purpose:** Read user data from a database and log filtered PII data using the configured logger
- **Output:** Log line with only non-PII fields and redacted sensitive fields
- **File:** `filtered_logger.py`

## 🔐 Example PII Fields

Examples of sensitive fields that must be redacted:
- `name`
- `email`
- `phone`
- `ssn`
- `password`

## 🛠️ Technologies Used

- Python 3.7
- MySQL
- `mysql-connector-python`
- `bcrypt`
- `logging` module
- `re` module for regex substitution
- Environment variables for credential security

## 🧼 Code Style

All code adheres strictly to the **PEP8** style guide with `pycodestyle==2.5`.

## 🧾 Usage

To run the main script:
```bash
PERSONAL_DATA_DB_USERNAME=root \
PERSONAL_DATA_DB_PASSWORD=root \
PERSONAL_DATA_DB_HOST=localhost \
PERSONAL_DATA_DB_NAME=my_db \
./filtered_logger.py

Author: Dzeble Kwame Baku
