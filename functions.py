from datetime import date
import os



def file_generator():
    file_today = date.today().strftime("%Y-%m-%d")
    new_file_name = f"Excel_Report_{file_today}.pdf"
    os.makedirs("Reports", exist_ok=True)

    return os.path.join("Reports", new_file_name)


