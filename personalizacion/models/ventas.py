#-*- coding: utf-8 -*-
from openerp import models, fields, api

class facturas(models.Model):
    _inherit = 'account.invoice.line'

    #precio_venta = fields.Float(string='Precio p venta', required=True, digits=dp.get_precision('Product Price'))

    monto = fields.Float(string='Monto',  compute='_compute_monto', store=True)
    itbis = fields.Float(string='Itbis',  compute='_compute_itbis', store=True)

    #campos con itbis excluido
    total = fields.Float(string='Total',  compute='_compute_total', store=True)
    itbi = fields.Float(string='Itbi',  compute='_compute_itbi', store=True)





    @api.depends('price_unit', 'quantity')
    def _compute_monto(self):
        for r in self:
            r.monto = r.price_unit*r.quantity

    @api.depends('price_unit', 'quantity','invoice_line_tax_ids')
    def _compute_itbis(self):
        for r in self:
            r.itbis = ((r.monto-r.price_subtotal))

    @api.depends('price_unit', 'quantity')
    def _compute_total(self):
        for r in self:
            r.total = r.price_subtotal+r.itbi

    @api.depends('price_unit', 'quantity')
    def _compute_itbi(self):
        for r in self:
            r.itbi = ((r.price_subtotal*.18))




class cotizacion(models.Model):
    _inherit = 'sale.order.line'

    monto = fields.Float(string='Monto',  compute='_compute_monto', store=True)
    itbis = fields.Float(string='Itbis',  compute='_compute_itbis', store=True)




    @api.depends('price_unit', 'product_uom_qty')
    def _compute_monto(self):
        for r in self:
            r.monto = r.price_unit*r.product_uom_qty

    @api.depends('price_unit', 'product_uom_qty')
    def _compute_itbis(self):
        for r in self:
            r.itbis = ((r.monto-r.price_subtotal))



