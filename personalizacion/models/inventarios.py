#-*- coding: utf-8 -*-
from openerp import models, fields, api

class productos(models.Model):
    _inherit = 'product.template'
    _order = "default_code"

    lst_price = fields.Float(related='precio_venta_itbis')

    list_price = fields.Float(related='precio_venta_itbis')

    
    medida = fields.Char(string='Medida', store=True)

    margen = fields.Float(string='Margen',  store=True)
    itbis = fields.Float(string='Itbis', store=True)

    precio_compra = fields.Float(string='Precio para Compra',  compute='_compute_compra', store=True)
    precio_venta = fields.Float(string='Precio para Venta',  compute='_compute_venta', store=True)
    precio_venta_itbis = fields.Float(string='Precio Venta con Itbis',  compute='_compute_venta_itbis', store=True)

    #precio_compra = fields.Float(string='Precio para Compra',  compute='_compute_compra', store=True)
    #precio_venta = fields.Float(string='Precio para Venta',  compute='_compute_venta', store=True)
    #precio_venta_itbis = fields.Float(string='Precio Venta con Itbis',  compute='_compute_venta_itbis', store=True)

    beneficio_margen = fields.Float(string='Beneficio', compute='_compute_beneficio', store=True)

    #list_price = fields.Float(compute='_compute_venta_precio')




    @api.depends('itbis','standard_price','margen')
    def _compute_compra(self):
        standard_price=self.standard_price;
        for r in self:
            r.precio_compra = (r.standard_price*r.itbis/100)+standard_price
    @api.depends('itbis','standard_price','margen')
    def _compute_venta(self):
        standard_price=self.standard_price;
        for r in self:
            r.precio_venta = (r.standard_price*r.margen/100)+standard_price
    @api.depends('itbis','standard_price','margen')
    def _compute_venta_itbis(self):
        precio_venta=self.precio_venta;
        for r in self:
            r.precio_venta_itbis = (r.precio_venta*r.itbis/100)+(precio_venta)

    @api.depends('margen')
    def _compute_beneficio(self):
        standard_price=self.standard_price;
        for r in self:
            r.beneficio_margen = (r.standard_price*r.margen/100)

   