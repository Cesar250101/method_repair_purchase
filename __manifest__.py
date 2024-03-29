# -*- coding: utf-8 -*-
{
    'name': "method_repair_purchase",

    'summary': """
        Crea abastecimiento en compras para los productos marcados como bajo pedido
        """,

    'description': """
        Genera un orden de compra para los productos que tenga la marca bajo
        pedido.
    """,

    'author': "Method",
    'website': "http://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','repair','sale'],

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
