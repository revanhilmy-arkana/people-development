# pyrefly: ignore [missing-import]
from odoo import fields, models

class SearchLesson(models.Model):
    _name = 'study.search.lesson'
    _description = 'Search Lesson'

    name = fields.Char(string='Title', required=True)
    category = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External')
    ], string='Category', default='internal')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority', default='medium')
    date = fields.Date(string='Date', default=fields.Date.today())
