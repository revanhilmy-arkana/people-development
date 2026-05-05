from odoo import api, fields, models

class StudyTag(models.Model):
    _name = 'study.lesson.tag'
    _description = 'Lesson Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color')
