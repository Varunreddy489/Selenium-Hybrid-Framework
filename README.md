# OrangeHRM Web Automation

This project contains automated tests for the OrangeHRM web application using modern web automation tools.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Running the Tests](#running-the-tests)

## Project Overview

This repository provides a suite of automated tests for the OrangeHRM platform. The goal is to ensure the reliability
and quality of the HRM system by automating key user workflows and regression scenarios.

## Features

- Automated login and logout tests
- Add Employee functionality
- Dashboard and reporting validations
- Search Employee functionality
- Cross-browser support

## Tech Stack

- **Programming Language:** Python
- **Automation Framework:** Selenium WebDriver
- **Test Runner:** pytest
- **Reporting:** HTML reports

## Getting Started

### Prerequisites

- Python 3.x
- pip
- Web drivers:
    - ChromeDriver (for Chrome)
    - GeckoDriver (for Firefox)
    - EdgeDriver (for Microsoft Edge)

### Installation

```
git clone https://github.com/Varunreddy489/Selenium-Hybrid-Framework

cd Selenium-Hybrid-Framework

pip install -r requirements.txt
```

## Project Structure

```
Python_Hybrid_Framework/
├── config/               # Configuration (e.g., config.ini)
├── logs/                 # Log output
├── page_objects/         # Page Object Model classes
├── reports/              # HTML reports
├── screenshots/          # Captured screenshots on failure
├── test_cases/           # Test scripts
├── test_data/            # External test data (if any)
├── utils/                # Utility modules (logger, config reader, etc.)
├── run.bat               # Windows batch script to run tests
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

```

## Running the Tests

### Running all tests

```
pytest test_cases/
```

### Run tests with specific markers:

Sanity tests:

```
pytest -v -s -m "sanity" --html=reports/report.html test_cases/ --browser chrome
```

Regression tests:
```
pytest -v -s -m "regression" --html=reports/report.html test_cases/ --browser firefox
```

Combine markers:
```
pytest -m "sanity or regression" --html=reports/report.html test_cases/
```
