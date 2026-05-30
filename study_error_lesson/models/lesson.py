from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError

class ErrorLesson(models.Model):
    _name = 'study.error.lesson'
    _description = 'Error and Validation Lesson'

    name = fields.Char(string='Student Name', required=True)
    age = fields.Integer(string='Age', default=0)
    email = fields.Char(string='Email Address')

    # CONSTRAINS: Triggered automatically on Save (Create/Write)
    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age < 0:
                # ValidationError is used for data checking
                raise ValidationError("Data Quality Alert! Age cannot be a negative number.")

    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            if rec.email and '@' not in rec.email:
                raise ValidationError("Format Error! Please enter a valid email address containing an '@' symbol.")

    # ACTION BUTTON: Triggered manually by clicking a button
    def action_check_validation(self):
        for rec in self:
            if rec.name == 'Test' or rec.name == 'test':
                # UserError is used for user actions/business flow blockers
                raise UserError("Action Blocked! You cannot validate a student named 'Test'. Please enter a real name.")

