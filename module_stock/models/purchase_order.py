# school_stock_management/models/purchase_order.py
from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _name = 'school.purchase.order'
    _description = 'Purchase Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    date_order = fields.Datetime(string='Order Date', required=True, default=fields.Datetime.now)
    order_line_ids = fields.One2many('school.purchase.order.line', 'order_id', string='Order Lines')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('school.purchase.order') or _('New')
        return super(PurchaseOrder, self).create(vals)

class PurchaseOrderLine(models.Model):
    _name = 'school.purchase.order.line'
    _description = 'Purchase Order Line'

    order_id = fields.Many2one('school.purchase.order', string='Order Reference', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    price_unit = fields.Float(string='Unit Price', required=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit

