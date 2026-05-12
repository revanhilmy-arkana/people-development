from odoo import api, fields, models

class ComputeLesson(models.Model):
    _name = 'study.compute.lesson'
    _description = 'Compute Field Lesson'

    name = fields.Char(string='Title', required=True)
    
    # Text calculation (Non-stored by default)
    upper_name = fields.Char(string='Upper Case Title', compute='_compute_upper_name')
    
    # Math calculation
    price = fields.Float(string='Price', default=0.0)
    tax = fields.Float(string='Tax Amount', default=0.0)
    
    # Stored calculation (Saved in database)
    total = fields.Float(string='Total Cost', compute='_compute_total', store=True)

    @api.depends('name')
    def _compute_upper_name(self):
        for rec in self:
            if rec.name:
                rec.upper_name = rec.name.upper()
            else:
                rec.upper_name = ""

    @api.depends('price', 'tax')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.price + rec.tax
