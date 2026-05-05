from odoo import api, fields, models, _

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Reference', default=lambda self: _('New'), readonly=True)
    age = fields.Integer(string='Age')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ref', _('New')) == _('New'):
                vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        return super(HospitalPatient, self).create(vals_list)
