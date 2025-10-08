import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from crewai.tools import Tool

@Tool
def save_report_as_pdf(report_text: str) -> str:
    """Save the generated report to a PDF file."""
    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"reports/financial_report_{timestamp}.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)
    text_obj = c.beginText(40, 750)
    text_obj.setFont("Helvetica", 11)

    for line in report_text.split("\n"):
        text_obj.textLine(line)
    c.drawText(text_obj)
    c.save()

    return f"📄 PDF report saved successfully at: {file_path}"
