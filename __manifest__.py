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
    'website': 'https://rosefilm.co',  # Optional: Replace with your website
    'depends': [
        'account',     # For accounting entries and journals
        'contacts',    # For customer and bank account information
        'sale',        # For integration with Sales Orders
        'purchase',    # For integration with Purchase Orders
    ],
    'data': [
        'security/ir.model.access.csv',          # Access controls for models
        'views/checkbook_views.xml',             # Views for managing checkbooks
        'views/cheque_views.xml',                # Views for cheque processing and workflows
        'views/category_views.xml',              # Views for category settings and accounting mappings
        'views/notification_views.xml',          # Views for notification and reminder settings
        'views/report_views.xml',                # Views for reports and analytics
        'reports/cheque_reports.xml',            # Report templates for cheque analytics
        'data/ir_cron_data.xml',                 # Scheduled actions for notifications
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
