# -*- coding: utf-8 -*-
{
    'name': "Personalizacion",

    'summary': """Personalizacion a medida para sistemas""",

    'description': """
        Desarrollo a medida
    """,

    'author': "Em Software",
    'website': "http://www.emsoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}