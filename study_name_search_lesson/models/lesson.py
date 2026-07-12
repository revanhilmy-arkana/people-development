from odoo import fields, models

class SearchTarget(models.Model):
    _name = 'study.name.search.target'
    _description = 'Name Search Target'
    
    # 1. Default field for display
    _rec_name = 'name'
    
    # 2. MODERN SEARCH (Odoo 17+):
    # This list defines which fields are checked when typing in a Many2one dropdown
    _rec_names_search = ['name', 'identification_id']

    name = fields.Char(string='Name', required=True)
    identification_id = fields.Char(string='ID Code', required=True)


class SearchReference(models.Model):
    _name = 'study.name.search.reference'
    _description = 'Name Search Reference'

    name = fields.Char(string='Title', required=True)
    # Many2one field to test the multi-field search
    target_id = fields.Many2one('study.name.search.target', string='Target Student')
