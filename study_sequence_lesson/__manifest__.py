{
    'name': 'Study Lesson: Sequences & Create Method',
    'version': '1.0',
    'category': 'Tutorial',
    'summary': 'Module to study Sequences, Many2one, Rec Name, and Create method overrides in Odoo 19.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
