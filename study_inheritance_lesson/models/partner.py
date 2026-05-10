# pyrefly: ignore [missing-import]
from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Is a Student?')
    student_rank = fields.Selection([
        ('junior', 'Junior'),
        ('senior', 'Senior')
    ], string='Student Rank')
