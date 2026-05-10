from odoo import api, fields, models

class StudyLesson(models.Model):
    _name = 'study.lesson.m2m'
    _description = 'Study Lesson Many2many'
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    tag_ids = fields.Many2many(
        'study.lesson.tag',
        string='Tags'
    )
    description = fields.Text(string='Description')
