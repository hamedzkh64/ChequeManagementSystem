# models/notification.py

from odoo import models, fields

class ChequeReminder(models.Model):
    _name = 'cheque_management.reminder'
    _description = 'Cheque Reminder'

    cheque_id = fields.Many2one('cheque_management.cheque', string="Cheque")
    reminder_date = fields.Date(string="Reminder Date")
    reminder_type = fields.Selection([
        ('upcoming', 'Upcoming Maturity'),
        ('return', 'Returned Cheque')
    ], string="Type", required=True)
    frequency = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ], string="Frequency")
    channel = fields.Selection([
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('whatsapp', 'WhatsApp')
    ], string="Notification Channel")
    recipient_ids = fields.Many2many('res.users', string="Recipients")
