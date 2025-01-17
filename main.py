from fpdf import FPDF
import glob
from pathlib import Path

#Create a list of text filepaths
filepaths = glob.glob("files/*.txt")
#Create one pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

#Go through each text file
for filepath in filepaths:
    pdf.add_page()

    #Get the filename without the extension and convert it to title case
    filename = Path(filepath).stem
    name = filename.title()

    #Add the name to pdf
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

#Produce the PDF
pdf.output("output.pdf")






