import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    this gets information about the bills to be paid by each of the flatmate, the period and generates a pdf report
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        #adds icon
        pdf.image("files/house.png", w=30, h=30)
        #insert title
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=60, txt="Flatmates Bill",  align="C", ln=1)
        #inseert period label and value
        pdf.cell(w=100, h=30, txt="Period", border=1)
        pdf.cell(w=150, h=30, txt=bill.period, border=1, ln=1)
        #name and amount of first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=30, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=30, txt=flatmate1.pays(bill, flatmate2), border=1, ln=1)
        # name and amount of second flatmate
        pdf.cell(w=100, h=30, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=30, txt=flatmate2.pays(bill, flatmate1), border=1, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename) #making the pdf file automatically open itself on the web browser