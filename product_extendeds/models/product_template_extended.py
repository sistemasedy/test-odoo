#-*- coding: utf-8 -*-
from openerp import models, fields, api

class ProductTemplateExtended(models.Model):
    _inherit = 'product.template'
    _order = "default_code"

    lst_price = fields.Float(related='price_sale_tax')

    list_price = fields.Float(related='price_sale_tax')

    
    measure = fields.Char(string='Measure', translate=True, store=True)

    margin = fields.Float(string='Margin', translate=True,  store=True)
    tax = fields.Float(string='Tax', translate=True, store=True)



    price_purchase = fields.Float(string='Price for Purchase', translate=True,  compute='_compute_purchase', store=True)
    price_sale = fields.Float(string='Price for Sale', translate=True,  compute='_compute_sale', store=True)
    price_sale_tax = fields.Float(string='Sale price with tax', translate=True,  compute='_compute_sale_tax', store=True)

    #precio_compra = fields.Float(string='Precio para Compra',  compute='_compute_compra', store=True)
    #precio_venta = fields.Float(string='Precio para Venta',  compute='_compute_venta', store=True)
    #precio_venta_itbis = fields.Float(string='Precio Venta con Itbis',  compute='_compute_venta_itbis', store=True)

    benefit_margin = fields.Float(string='Benefit', translate=True, compute='_compute_benefit', store=True)

    #list_price = fields.Float(compute='_compute_venta_precio')




    @api.depends('tax','standard_price','margin')
    def _compute_purchase(self):
        standard_price=self.standard_price;
        for r in self:
            r.price_purchase = (r.standard_price*r.tax/100)+standard_price
    @api.depends('tax','standard_price','margin')
    def _compute_sale(self):
        standard_price=self.standard_price;
        for r in self:
            r.price_sale = (r.standard_price*r.margin/100)+standard_price
    @api.depends('tax','standard_price','margin')
    def _compute_sale_tax(self):
        price_sale=self.price_sale;
        for r in self:
            r.price_sale_tax = (r.price_sale*r.tax/100)+(price_sale)

    @api.depends('margin')
    def _compute_benefit(self):
        standard_price=self.standard_price;
        for r in self:
            r.benefit_margin = (r.standard_price*r.margin/100)

   