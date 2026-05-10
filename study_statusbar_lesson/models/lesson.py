# pyrefly: ignore [missing-import]
from odoo import api, fields, models

class StatusbarLesson(models.Model):
    _name = "study.statusbar.lesson"
    _description = "Statusbar Lesson"

    name = fields.Char(string="Reference", required=True, default="New")
    description = fields.Text(string="Description")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft', string="Status", required=True)
    
    # Example field to show conditional invisible
    hide_me = fields.Char(string="Secret Field", help="Visible only in Done state")

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
            
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
