from odoo import models, fields

class ArticleType(models.Model):
    _name = 'inventory.article.type'
    _description = 'Article Type'

    name = fields.Char(string='Article Name', required=True)
    block = fields.Char(string='Block')
    room = fields.Char(string='Room/Administration')
    year_received = fields.Integer(string='Year Received')
    ticket_pdf = fields.Binary('Ticket PDF', readonly=True)
    ticket_filename = fields.Char('Ticket Filename', readonly=True)

    def generate_ticket(self):
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from io import BytesIO
        import base64

        for record in self:
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            p.drawString(100, 750, f"Article Name: {record.name}")
            p.drawString(100, 735, f"Block: {record.block}")
            p.drawString(100, 720, f"Room/Administration: {record.room}")
            p.drawString(100, 705, f"Year Received: {record.year_received}")
            # Here you can add code to generate a barcode or QR code
            p.showPage()
            p.save()

            buffer.seek(0)
            pdf = buffer.getvalue()
            buffer.close()

            record.write({
                'ticket_pdf': base64.b64encode(pdf),
                'ticket_filename': f"{record.name}_ticket.pdf",
            })
