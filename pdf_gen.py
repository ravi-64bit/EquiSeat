"""PDF export for generated room seating charts."""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle


def generate_pdfs_for_matrices(matrices, room_names=None, output_dir="."):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    generated = []
    room_names = room_names or []
    for index, item in enumerate(matrices, start=1):
        if isinstance(item, tuple) and len(item) == 2:
            room_name, matrix = item
        else:
            room_name = room_names[index - 1] if index <= len(room_names) else f"Room {index}"
            matrix = item
        if not matrix or not matrix[0]:
            continue
        page = landscape(A4) if len(matrix[0]) >= len(matrix) else A4
        page_width, page_height = page
        usable_width, usable_height = page_width - inch, page_height - 1.5 * inch
        cols, rows = len(matrix[0]), len(matrix)
        cell_width = usable_width / cols
        cell_height = usable_height / rows
        data = [["" if value is None else str(value) for value in row] for row in matrix]
        table = Table(data, colWidths=[cell_width] * cols, rowHeights=[cell_height] * rows)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 0.8, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
        ]))
        safe_name = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in room_name)
        filename = f"seating_{safe_name}.pdf"
        from reportlab.pdfgen.canvas import Canvas
        canvas = Canvas(str(output / filename), pagesize=page)
        canvas.setTitle(f"EquiSeat - {room_name}")
        canvas.setFont("Helvetica-Bold", 16)
        canvas.drawCentredString(page_width / 2, page_height - 0.45 * inch, f"Seating Arrangement: {room_name}")
        table.wrapOn(canvas, usable_width, usable_height)
        table.drawOn(canvas, 0.5 * inch, page_height - inch - rows * cell_height)
        canvas.save()
        generated.append(filename)
    return generated
