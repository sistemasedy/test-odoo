# -*- coding: utf-8 -*-
from odoo import http

# class Personalizacion(http.Controller):
#     @http.route('/personalizacion/personalizacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/personalizacion/personalizacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('personalizacion.listing', {
#             'root': '/personalizacion/personalizacion',
#             'objects': http.request.env['personalizacion.personalizacion'].search([]),
#         })

#     @http.route('/personalizacion/personalizacion/objects/<model("personalizacion.personalizacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('personalizacion.object', {
#             'object': obj
#         })