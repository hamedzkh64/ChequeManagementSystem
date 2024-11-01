# models/cheque.py

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

    @api.model
    def create_account_move(self, debit_account, credit_account, amount, journal, ref):
        """Create an accounting move entry"""
        move = self.env['account.move'].create({
            'ref': ref,
            'journal_id': journal.id,
            'line_ids': [
                (0, 0, {
                    'account_id': debit_account.id,
                    'debit': amount,
                }),
                (0, 0, {
                    'account_id': credit_account.id,
                    'credit': amount,
                }),
            ],
        })
        move.action_post()  # Automatically post the move
        return move

    def action_receive_cheque(self):
        """Action to receive a cheque and update accounting entries."""
        self.ensure_one()
        if self.status != 'in_vault':
            raise ValidationError("Cheque must be in vault to receive.")
        self.status = 'in_vault'
        self.create_account_move(
            self.category_id.debit_account_id,
            self.category_id.credit_account_id,
            self.amount,
            self.category_id.journal_id,
            ref=f"Received Cheque - {self.check_number}"
        )

    def action_issue_cheque(self):
        """Action to issue a cheque for payment."""
        self.ensure_one()
        if self.status != 'in_vault':
            raise ValidationError("Cheque must be in vault to issue.")
        self.status = 'issued'
        self.create_account_move(
            self.category_id.debit_account_id,
            self.category_id.credit_account_id,
            self.amount,
            self.category_id.journal_id,
            ref=f"Issued Cheque - {self.check_number}"
        )

    def action_endorse_cheque(self):
        """Endorse cheque to a third party."""
        self.ensure_one()
        if self.status != 'in_vault' and self.status != 'issued':
            raise ValidationError("Cheque must be in vault or issued to endorse.")
        self.status = 'endorsed'
        self.create_account_move(
            self.category_id.debit_account_id,
            self.category_id.credit_account_id,
            self.amount,
            self.category_id.journal_id,
            ref=f"Endorsed Cheque - {self.check_number}"
        )

    def action_transfer_cheque(self):
        """Transfer cheque to the bank."""
        self.ensure_one()
        if self.status != 'in_vault' and self.status != 'issued' and self.status != 'endorsed':
            raise ValidationError("Cheque must be in vault, issued, or endorsed to transfer.")
        self.status = 'transferred'
        self.create_account_move(
            self.category_id.debit_account_id,
            self.category_id.credit_account_id,
            self.amount,
            self.category_id.journal_id,
            ref=f"Transferred Cheque - {self.check_number}"
        )
