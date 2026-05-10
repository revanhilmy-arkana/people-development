# pyrefly: ignore [missing-import]
from odoo import fields, models

class NotebookLesson(models.Model):
    _name = 'study.notebook.lesson'
    _description = 'Notebook Lesson'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    internal_notes = fields.Text(string='Internal Notes')
    active = fields.Boolean(string='Active', default=True)
    sequence = fields.Integer(string='Sequence', default=10)
    date_recorded = fields.Date(string='Date', default=fields.Date.today())
