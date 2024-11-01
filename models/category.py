# models/category.py

from odoo import models, fields

class ChequeCategory(models.Model):
    _name = 'cheque_management.category'
    _description = 'Cheque Category'

    name = fields.Char(string="Category Name", required=True)
    account_type = fields.Selection([
        ('income', 'Income'), 
        ('expense', 'Expense'), 
        ('receivable', 'Receivable'), 
        ('payable', 'Payable')
    ], required=True)
    debit_account_id = fields.Many2one('account.account', string="Debit Account")
    credit_account_id = fields.Many2one('account.account', string="Credit Account")
    journal_id = fields.Many2one('account.journal', string="Journal")
    description = fields.Text(string="Description")
