#Excel Report PDF Generator
import pandas as pd
from fpdf import FPDF
from fpdf.fonts import FontFace
from pdf_builder import InvoicePDF, add_invoice_table, add_summary
from functions import file_generator, load_data, save_pdf

df = load_data("Data/sample_invoices_small.xlsx", "Invoices")
if df is None:
    exit()

# print first 5 rows
#print(df.head())

#print the column names
#print(df.columns)

#print the data types per column
#print(df.dtypes)


#need to show popular choices
#total amount per client name
#average per client
#number of invoices per client

records = df.to_dict('records')

total = 0
count = 0
pending = []

for record in records:
    try: 
        amount = float(record['Amount'])
        total += amount
        count += 1
    except ValueError:
        pending.append(record)

print(f"Total: {total:.2f}")
print(pending)
print()
print(total/count)




pdf = InvoicePDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.ln(1)
add_invoice_table(pdf, records)
add_summary(pdf, total, count, pending)
save_pdf(pdf)
