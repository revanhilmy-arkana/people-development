from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='Doctor Name', required=True)
    specialty = fields.Char(string='Specialty')
