from odoo import fields, models, api
from odoo.exceptions import UserError

class UnlinkLesson(models.Model):
    _name = 'study.unlink.lesson'
    _description = 'Unlink Method Lesson'

    name = fields.Char(string='Title', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('locked', 'Locked')
    ], string='Status', default='draft')

    # OVERRIDING THE DELETE METHOD
    def unlink(self):
        for rec in self:
            # Custom logic: Prevent deletion if status is 'locked'
            if rec.state == 'locked':
                # UserError will stop the process and show a message
                raise UserError("Action Blocked! You cannot delete a record that is in 'Locked' state.")
        
        # Super() calls the original Odoo delete method to finish the job
        return super(UnlinkLesson, self).unlink()
