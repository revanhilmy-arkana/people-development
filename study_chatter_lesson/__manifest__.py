{
    'name': 'Study Chatter Lesson',
    'version': '1.0',
    'summary': 'Module for studying Chatter (mail.thread), Field Tracking, and Activities in Odoo 19',
    'category': 'Education',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
