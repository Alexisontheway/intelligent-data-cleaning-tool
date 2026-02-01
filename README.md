Intelligent Data Cleaning & Analysis Tool (Python)

A professional, CLI-based Python tool for cleaning CSV datasets and generating transparent data quality reports.
Designed with modular architecture, safety-first execution, and real-world data engineering practices.

🚀 Features

CSV Data Cleaning Pipeline

Normalize column names

Handle missing values conservatively

Remove duplicate records

Dry-Run Mode

Preview the cleaning process without writing output files

Safe for production and large datasets

Data Quality Reporting

Automatically generates a human-readable report

Summarizes row counts, duplicates removed, and missing values

Command-Line Interface (CLI)

Clear help text and argument descriptions

Easy to integrate into scripts or automation workflows

🧠 Design Philosophy

This project focuses on data integrity, transparency, and modularity:

Cleaning logic is separated from reporting

No aggressive or guess-based data modification

Every transformation is observable and explainable

Built incrementally in phases, mirroring real software development workflows

📁 Project Structure
intelligent-data-cleaning-tool/
│
├── data_cleaner/
│   ├── loader.py        # Safe CSV loading
│   ├── cleaner.py       # Data cleaning logic
│   └── reporter.py      # Reporting & output utilities
│
├── main.py              # CLI entry point
├── test_data.csv        # Sample input dataset
├── data_quality_report.txt
├── requirements.txt
└── README.md

▶️ How to Run
1️⃣ Normal Execution
python main.py test_data.csv cleaned_data.csv


Cleans the input dataset

Saves the cleaned CSV

Generates a data quality report

2️⃣ Dry-Run Mode (Recommended for Safety)
python main.py test_data.csv cleaned_data.csv --dry-run


Runs all validations and analysis

Generates the data quality report

Does NOT create the cleaned CSV

3️⃣ CLI Help
python main.py --help


Displays usage instructions and available options.

📊 Sample Data Quality Report
DATA QUALITY REPORT
===================

Original rows: 6
Final rows: 5
Duplicates removed: 1

Missing values by column:
- purchase_amount: 1

🛠 Technologies Used

Python

Pandas

argparse

pathlib

logging

📈 Development Phases

Phase 1: Core data cleaning pipeline

Phase 2: CLI improvements and dry-run mode

Phase 3: Data quality report generation

Each phase was committed separately to maintain a clean and traceable development history.

🎯 Use Cases

Data preprocessing for analytics or ML pipelines

CSV quality validation before ingestion

Automation-friendly cleaning for batch workflows

Demonstration of real-world Python engineering skills

👤 Author

Priyanshu Pramanik
Computer Science Undergraduate
Focused on Python, data engineering fundamentals, and automation tooling.

📌 Notes

This project prioritizes clarity, safety, and correctness over aggressive automation.
Future enhancements may include configurable report paths, multiple report formats (CSV/JSON), and batch processing support.
