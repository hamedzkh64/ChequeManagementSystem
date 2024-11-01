# models/cheque.py

from odoo import models, fields

class Cheque(models.Model):
    _name = 'cheque_management.cheque'
    _description = 'Cheque Management'

    check_number = fields.Char(string="Check Number", required=True)
    saad_number = fields.Char(string="Saad Number", required=True)
    amount = fields.Float(string="Amount", required=True)
    issue_date = fields.Date(string="Issue Date", required=True)
    maturity_date = fields.Date(string="Maturity Date", required=True)
    status = fields.Selection([
        ('in_vault', 'In Vault'),
        ('issued', 'Issued'),
        ('endorsed', 'Endorsed'),
        ('transferred', 'Transferred'),
        ('cleared', 'Cleared'),
        ('returned', 'Returned')
    ], default='in_vault', string="Status")
    customer_id = fields.Many2one('res.partner', string="Customer", domain="[('customer_rank', '>', 0)]", required=True)
    issuer_name = fields.Char(string="Issuer's Name")
    issuer_national_id = fields.Char(string="Issuer's National ID")
    category_id = fields.Many2one('cheque_management.category', string="Category", required=True)
    checkbook_id = fields.Many2one('cheque_management.checkbook', string="Checkbook")
