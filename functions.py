from datetime import date
import os
import pandas as pd

def file_generator():
    file_today = date.today().strftime("%Y-%m-%d")
    new_file_name = f"Excel_Report_{file_today}.pdf"
    os.makedirs("Reports", exist_ok=True)

    return os.path.join("Reports", new_file_name)


def load_data(path, sheet):
    try:
         return pd.read_excel(path, sheet_name = sheet)
    
    except FileNotFoundError:
        print("File not found, Check the path.")
        return None 
    
    except ValueError:
        print("sheet does not exist")
        return None

def save_pdf(pdf):
    try:
        pdf.output(file_generator())
    except PermissionError:
        print("could not save the PDF. Is it open in another program?")
        
