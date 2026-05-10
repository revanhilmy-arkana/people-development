# pyrefly: ignore [missing-import]
from odoo import fields, models

class RelatedStudent(models.Model):
    _name = 'study.related.student'
    _description = 'Related Student (Source)'

    name = fields.Char(string='Student Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')


class RelatedLesson(models.Model):
    _name = 'study.related.lesson'
    _description = 'Related Lesson (Target)'

    name = fields.Char(string='Title', required=True)
    student_id = fields.Many2one('study.related.student', string='Student')
    
    # RELATED FIELDS:
    # They pull values from 'student_id' automatically
    student_email = fields.Char(related='student_id.email', string='Student Email', readonly=True)
    student_phone = fields.Char(related='student_id.phone', string='Student Phone', readonly=True)
    
    # Using store=True makes it searchable and filterable in the database
    student_name_stored = fields.Char(related='student_id.name', string='Student Name (Stored)', store=True)
