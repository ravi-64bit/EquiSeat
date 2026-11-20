from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def generate_pdfs_for_matrices(matrices):
    for i, matrix in enumerate(matrices):
        rows = len(matrix)
        cols = len(matrix[0])

        
        cell_width = (A4[0] - 2 * inch) / cols
        cell_height = (A4[1] - 2 * inch) / rows

        data = [[str(value) for value in row] for row in matrix]

        styles = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica')  
        ])

        table = Table(data, repeatRows=1, colWidths=[cell_width] * cols, rowHeights=[cell_height] * rows)
        table.setStyle(styles)

        pdf_name = f"matrix_{i+1}.pdf"

        c = canvas.Canvas(pdf_name, pagesize=A4)
        table.wrapOn(c, A4[0] - 2 * inch, A4[1] - 2 * inch)
        table.drawOn(c, 1 * inch, 1 * inch)
        c.save()

