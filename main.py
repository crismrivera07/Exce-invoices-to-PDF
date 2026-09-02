#Excel Report PDF Generator
import pandas as pd
from fpdf import FPDF
from fpdf.fonts import FontFace
from pdf_builder import InvoicePDF, add_invoice_table


df = pd.read_excel("Data/sample_invoices_small.xlsx", sheet_name = "Invoices")

"""
# print first 5 rows
print(df.head())

#print the column names
print(df.columns)

#print the data types per column
print(df.dtypes)"""


#need to show popular choices
#total amount per client name
#average per client
#number of invoices per client

records = df.to_dict('records')
print(df.groupby(['Client Name','Item Description'])['Quantity'].sum())

print()
print(df.groupby('Client Name')['Invoice ID'].count())
















"""
pdf = InvoicePDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
add_invoice_table(pdf, records)
pdf.output("Exel Generator.pdf")"""