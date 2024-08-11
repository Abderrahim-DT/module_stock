from odoo import models, fields, api

class Beneficiary(models.Model):
    _name = 'school.beneficiary1'
    _description = 'Beneficiary'

    name = fields.Char(string='Beneficiary Name', required=True)
    department = fields.Char(string='Department')
    purchase_order_id = fields.Many2one('school.purchase.order', string='Purchase Order', required=True)
    beneficiary_line_ids = fields.One2many('school.beneficiary1.line', 'beneficiary_id', string='Beneficiary Lines')

    @api.onchange('purchase_order_id')
    def _onchange_purchase_order_id(self):
        if self.purchase_order_id:
            lines = []
            for line in self.purchase_order_id.order_line_ids:
                lines.append((0, 0, {
                    'product_id': line.product_id.id,
                    'quantity': line.product_uom_qty,  # Utilisez le champ correct pour la quantité
                    'purchase_order_id': self.purchase_order_id.id,
                }))
            self.beneficiary_line_ids = lines


class BeneficiaryLine(models.Model):
    _name = 'school.beneficiary1.line'
    _description = 'Beneficiary Line'

    beneficiary_id = fields.Many2one('school.beneficiary1', string='Beneficiary', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    purchase_order_id = fields.Many2one('school.purchase.order', string='Purchase Order', required=True)
