# Excel Invoices → PDF Report Generator

🚧 **Status:** In progress

A Python script that reads invoice data from an Excel (`.xlsx`) file, aggregates it, and generates a formatted PDF report.

## Overview

- **Input:** Excel file with invoice/line-item rows
- **Output:** A formatted PDF report with a table of invoices and summary totals
- **Why:** Third portfolio project — builds on PDF generation skills from a previous project, adds Excel data handling and aggregation logic

## Tech Stack

- Python 3.11
- `openpyxl` / `pandas` — reading Excel data
- `fpdf2` — generating the PDF

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

_(update once the actual run command/args are finalized)_

## Example Output

_(add a screenshot or sample PDF once one exists)_

## What I Learned

_(fill in as you go — tricky bugs, new concepts, things you'd do differently)_

## Project Structure

```
Excel-invoices-to-PDF/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```