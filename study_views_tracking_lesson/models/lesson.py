# pyrefly: ignore [missing-import]
from odoo import fields, models

class ViewsTrackingLesson(models.Model):
    _name = 'study.views.tracking'
    _description = 'Views and Tracking Lesson'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', tracking=True)
    note = fields.Text(string='Note')
