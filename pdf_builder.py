from fpdf import FPDF

class InvoicePDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(40, 10, "Excel Report", border=1, align="C")
        # Performing a line break:
        self.ln(15)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="I", size=8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def add_invoice_table(pdf,records):
    for record in records:
        pdf.cell(40, 10, record["Invoice ID"], align="L")
        pdf.cell(60, 10, record["Client Name"],new_y="NEXT", new_x="LMARGIN")


