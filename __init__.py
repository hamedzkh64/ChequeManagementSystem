# cheque_management/__manifest__.py
{
    'name': 'Cheque Management System',
    'version': '1.0',
    'author': 'Rosefilm',
    'category': 'Accounting',
    'summary': 'Module to manage cheque operations in Odoo',
    'description': """
    A comprehensive cheque management system to handle all aspects of cheque processing within the Accounting Module.
    """,
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/cheque_management_views.xml',
    ],
    'installable': True,
    'application': True,
}
