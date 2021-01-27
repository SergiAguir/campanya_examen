# -*- coding: utf-8 -*-
{
    'name': "cooperativa",

    'summary': """
        examen""",

    'description': """
        examen
    """,

    'author': "Sergi Agúir",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/campanya_view.xml',
        'views/productos_view.xml',
        'views/socios_view.xml',
        'views/menu_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,
}
