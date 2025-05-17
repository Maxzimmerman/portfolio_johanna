from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Image
from reportlab.pdfgen.canvas import Canvas
from datetime import datetime

class CreatePdf:
    def __init__(self, costumer_name, date, table, further_movements, suggestion, legend_data, result):
        self.costumer_name = costumer_name
        self.date = date
        self.table = table
        self.further_movements = further_movements
        self.suggestion = suggestion
        self.legend_data = legend_data
        self.result = result

    def draw_footer(self, canvas, doc):
        canvas.saveState()
        width, height = A4
        footer_text1 = "Johanna Zimmermann · Hanauer Straße 27, 63546 Hammersbach · Mobil: 0151/15565862"
        footer_text2 = "E-Mail: zimmermannjohanna233@gmail.com · www.johanna-zimmermann.com"

        canvas.setFont('Helvetica', 9)
        canvas.drawCentredString(width / 2.0, 30, footer_text1)
        canvas.drawCentredString(width / 2.0, 18, footer_text2)
        canvas.restoreState()

    def create(self):
        filename = "portfolio/services/behandlungsuebersicht.pdf"

        # Create document
        doc = SimpleDocTemplate(filename, pagesize=A4,
                                rightMargin=50, leftMargin=50,
                                topMargin=32, bottomMargin=50)

        styles = getSampleStyleSheet()
        elements = []

        # styles
        centered_style = ParagraphStyle(
            name='CenteredStyle',
            parent=styles['Normal'],
            alignment=TA_CENTER,     # Center the text
            fontSize=10,             # Set desired font size
        )

        # Add logo at the top of the PDF
        logo = Image("portfolio/services/logo.jpg", width=100, height=100)
        logo.hAlign = 'RIGHT'
        elements.append(logo)

        # Title
        elements.append(Paragraph("Behandlungsübersicht", styles['Title']))
        elements.append(Spacer(1, 20))

        # Date and name
        elements.append(Paragraph(f"{self.costumer_name}, {self.date}", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Befund:</b> {self.result}", styles['Normal']))
        elements.append(Spacer(1, 12))



        if self.table:
            # Convert text in data into Paragraphs to handle text wrapping
            wrapped_data = []
            for row in self.table:
                wrapped_row = [Paragraph(cell, styles['Normal']) for cell in row]
                wrapped_data.append(wrapped_row)

            # only take columns which are not an empty string
            #wrapped_elements = [[first, second] for first, second in wrapped_data if second != ""]

            # Create table
            table = Table(wrapped_data, colWidths=[doc.pagesize[0] * 0.50 - 55, doc.pagesize[0] * 0.50 - 55])  # 50% of page width

            # Style table
            table.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))

            elements.append(table)

        # further movements
        elements.append(Spacer(1, 10))
        elements.append(Paragraph("<b>Weitere Bewegung:</b>", styles['Normal']))

        elements.append(Spacer(1, 10))
        elements.append(Paragraph(f"{self.further_movements}", styles['Normal']))
        elements.append(Spacer(1, 10))

        # suggestions
        elements.append(Spacer(1, 10))
        elements.append(Paragraph("<b>Empfehlung:</b>", styles['Normal']))

        elements.append(Spacer(1, 10))
        elements.append(Paragraph(f"{self.suggestion}", styles['Normal']))
        elements.append(Spacer(1, 10))

        # legend_data table
        elements.append(Spacer(1, 10))
        elements.append(Paragraph("<b>Legende:</b>", styles['Normal']))

        if self.legend_data:
            wrapped_legend_data = []
            for row in self.legend_data:
                wrapped_row = [Paragraph(cell, styles['Normal']) for cell in row]
                wrapped_legend_data.append(wrapped_row)

            legend_table = Table(wrapped_legend_data, colWidths=[
                doc.pagesize[0] * 0.25 - 25,
                doc.pagesize[0] * 0.25 - 25,
                doc.pagesize[0] * 0.25 - 25,
                doc.pagesize[0] * 0.25 - 25
            ])

            legend_table.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 5),
            ]))

            elements.append(legend_table)


        # Build PDF
        doc.build(elements, onFirstPage=self.draw_footer, onLaterPages=self.draw_footer)
        print("PDF created successfully.")
