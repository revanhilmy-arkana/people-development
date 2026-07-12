from odoo import fields, models

class ChatterLesson(models.Model):
    _name = 'study.chatter.lesson'
    _description = 'Chatter and Activity Lesson'
    
    # 1. Inheriting mail.thread and mail.activity.mixin provides chatter capability
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # 2. tracking=True keeps a log in the chatter when the value of the field changes
    name = fields.Char(string='Lesson Title', required=True, tracking=True)
    description = fields.Text(string='Content Description')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string='Status', default='draft', tracking=True)

    responsible_id = fields.Many2one('res.users', string='Responsible Teacher', tracking=True, default=lambda self: self.env.user)
