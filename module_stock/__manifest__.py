# school_stock_management/__manifest__.py
{
    'name': 'ENSA stock',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Custom module to manage stock for an engineering school',
    'author': 'Your Name',
    'depends': ['base', 'stock', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/report_actions.xml',
        'views/report_templates.xml',
        'views/purchase_order_views.xml',
        'views/beneficiary_views.xml',
        'views/report_menu_views.xml',
        'data/data.xml',
    ],
    'installable': True,
    'application': True,
}
