# __manifest__.py

{
    'name': 'Comprehensive Cheque Management System',
    'version': '1.0',
    'summary': 'Manage cheque operations with full accounting integration, reminders, and reporting',
    'description': """
        This module covers comprehensive cheque processing within Odoo, including issuance, endorsement, transfer to bank, return handling, automated accounting entries, and due date notifications.
    """,
    'category': 'Accounting',
    'author': 'Your Name',
    'depends': ['account', 'contacts', 'sale', 'purchase'],  # Including relevant modules for full integration
    'data': [
        'security/ir.model.access.csv',
        'views/checkbook_views.xml',
        'views/cheque_views.xml',
        'views/category_views.xml',
        'views/notification_views.xml',
        'views/report_views.xml',
        'reports/cheque_reports.xml',
    ],
    'installable': True,
    'application': True,
}
