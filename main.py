#Excel Report PDF Generator
import pandas as pd
from fpdf import FPDF
from fpdf.fonts import FontFace
from pdf_builder import InvoicePDF, add_invoice_table


df = pd.read_excel("Data/sample_invoices_small.xlsx", sheet_name = "Invoices")


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


#print("Total Item installs")
#print(df.groupby(['Client Name','Item Description'])['Quantity'].sum())


#print("invoice count")
#print(df.groupby(['Client Name','Invoice ID'])['Amount'].count())

#print(df['Amount'].dtype)
#print(df.groupby(['Client Name'])['Amount'].mean())


















"""
pdf = InvoicePDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
add_invoice_table(pdf, records)
pdf.output("Exel Generator.pdf")"""