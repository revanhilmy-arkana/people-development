from odoo import api, fields, models
from odoo.exceptions import UserError

class WriteLesson(models.Model):
    _name = 'study.write.lesson'
    _description = 'Write Method Lesson'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Content Description')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('locked', 'Locked')
    ], string='Status', default='draft')

    last_editor = fields.Char(string='Last Edited By', readonly=True)
    edit_count = fields.Integer(string='Edit Count', default=0, readonly=True)

    # OVERRIDING THE WRITE (UPDATE) METHOD
    # In Odoo, 'vals' is a dictionary containing only the fields being updated
    def write(self, vals):
        # 1. Custom Check: Prevent editing the Title if the record is locked
        for rec in self:
            if rec.state == 'locked':
                # If they try to change the name or description while locked, block it
                if 'name' in vals or 'description' in vals:
                    raise UserError("Blocked! You cannot modify the Title or Description of a LOCKED record.")

        # 2. Automated Action: Track edit counts and last editors
        # We append these updates to the 'vals' dictionary before saving
        vals['last_editor'] = self.env.user.name
        # Note: Since edit_count is readonly, we increment it behind the scenes
        for rec in self:
            vals['edit_count'] = rec.edit_count + 1

        # 3. Call super() to let Odoo write the modifications to the database
        return super(WriteLesson, self).write(vals)
