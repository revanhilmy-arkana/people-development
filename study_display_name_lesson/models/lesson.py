from odoo import api, fields, models

class DisplayNameLesson(models.Model):
    _name = 'study.display.name'
    _description = 'Display Name Lesson'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)

    # MODERN WAY (Odoo 17+): Overriding _compute_display_name
    # This replaces the old name_get() method
    def _compute_display_name(self):
        for rec in self:
            if rec.code and rec.name:
                rec.display_name = f"[{rec.code}] {rec.name}"
            else:
                # Fallback to standard name if fields are empty
                rec.display_name = rec.name or rec.code or "New Record"


class DisplayReference(models.Model):
    _name = 'study.display.reference'
    _description = 'Display Reference'

    name = fields.Char(string='Title', required=True)
    # Many2one field to see the formatted name in action
    display_record_id = fields.Many2one('study.display.name', string='Display Record')
