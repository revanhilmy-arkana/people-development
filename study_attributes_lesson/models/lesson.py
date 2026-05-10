# pyrefly: ignore [missing-import]
from odoo import fields, models

class AttributesLesson(models.Model):
    _name = 'study.attributes.lesson'
    _description = 'Attributes Lesson'

    name = fields.Char(string='Title', required=True)
    is_priority = fields.Boolean(string='Is Priority?')
    priority_reason = fields.Text(string='Priority Reason')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('locked', 'Locked')
    ], string='Status', default='draft')
