from flat import Bill, Flatmate
from report import PdfReport

amount = int(input("How much is the bill to be shared? "))
period = input("The bill is for which month/period? ")
fmate1_name = input("What's the name of the flatmate: ")
fmate1_days = int(input(f"How many days did {fmate1_name} spend in the house? "))
fmate2_name = input("What's the name of the other flatmate: ")
fmate2_days = int(input(f"How many days did {fmate2_name} spend in the house? "))

fmate1 = Flatmate(fmate1_name, fmate1_days)
fmate2 = Flatmate(fmate2_name, fmate2_days)
bill = Bill(amount, period)

pdf_report = PdfReport("Report1.pdf")
pdf_report.generate(fmate1, fmate2, bill)