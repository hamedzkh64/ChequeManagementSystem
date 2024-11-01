# models/checkbook.py

from odoo import models, fields, api

class Checkbook(models.Model):
    _name = 'cheque_management.checkbook'
    _description = 'Checkbook Management'

    name = fields.Char(string="Checkbook Name", required=True)
    bank_account_id = fields.Many2one('res.partner.bank', string="Bank Account", required=True)
    bank_name = fields.Char(related='bank_account_id.bank_name', string="Bank Name", readonly=True)
    branch = fields.Char(string="Branch")
    total_leaves = fields.Integer(string="Total Number of Leaves", required=True)
    starting_check_number = fields.Integer(string="Starting Check Number", required=True)
    starting_serial_number = fields.Integer(string="Starting Serial Number", default=1)
    starting_saad_number = fields.Integer(string="Starting Saad Number", default=1)
    leaf_ids = fields.One2many('cheque_management.chequeleaf', 'checkbook_id', string="Cheque Leaves")

    @api.model
    def create(self, vals):
        record = super(Checkbook, self).create(vals)
        for i in range(vals['total_leaves']):
            self.env['cheque_management.chequeleaf'].create({
                'checkbook_id': record.id,
                'check_number': vals['starting_check_number'] + i,
                'serial_number': vals['starting_serial_number'] + i,
                'saad_number': vals['starting_saad_number'] + i,
            })
        return record


class ChequeLeaf(models.Model):
    _name = 'cheque_management.chequeleaf'
    _description = 'Cheque Leaf'

    checkbook_id = fields.Many2one('cheque_management.checkbook', string="Checkbook", ondelete="cascade")
    check_number = fields.Integer(string="Check Number", required=True)
    serial_number = fields.Integer(string="Serial Number")
    saad_number = fields.Integer(string="Saad Number")
    status = fields.Selection([('available', 'Available'), ('issued', 'Issued')], default='available')
