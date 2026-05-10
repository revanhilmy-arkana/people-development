# pyrefly: ignore [missing-import]
from odoo import fields, models

class One2manyLesson(models.Model):
    _name = 'study.one2many.lesson'
    _description = 'One2many Lesson'

    name = fields.Char(string='Lesson Title', required=True)
    description = fields.Text(string='Description')
    
    # One2many field: 
    # 1. Target model name ('study.one2many.line')
    # 2. Back-reference field on target model ('lesson_id')
    line_ids = fields.One2many('study.one2many.line', 'lesson_id', string='Lesson Lines')


class One2manyLine(models.Model):
    _name = 'study.one2many.line'
    _description = 'One2many Lesson Line'

    # The Many2one field that "points back" to the parent
    lesson_id = fields.Many2one('study.one2many.lesson', string='Parent Lesson', ondelete='cascade')
    
    name = fields.Char(string='Topic', required=True)
    note = fields.Char(string='Note')
