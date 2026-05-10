# pyrefly: ignore [missing-import]
from odoo import fields, models, api

class SecurityLesson(models.Model):
    _name = 'study.security.lesson'
    _description = 'Security Lesson'

    name = fields.Char(string='Title', required=True)
    user_id = fields.Many2one('res.users', string='Responsible User', default=lambda self: self.env.user)
    description = fields.Text(string='Private Notes')
