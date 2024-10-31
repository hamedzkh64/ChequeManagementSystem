# cheque_management/models/cheque.py
from odoo import models, fields, api

class Cheque(models.Model):
    _name = 'cheque.management.cheque'
    _description = 'Cheque Management'

    number = fields.Char(string="Cheque Number", required=True)
    saad_number = fields.Char(string="Saad Number")
    amount = fields.Float(string="Amount", required=True)
    issue_date = fields.Date(string="Issue Date", required=True)
    maturity_date = fields.Date(string="Maturity Date", required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('issued', 'Issued'),
        ('cleared', 'Cleared'),
        ('returned', 'Returned')
    ], default='draft', string="Status")
