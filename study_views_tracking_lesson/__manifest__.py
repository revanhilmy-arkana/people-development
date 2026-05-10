{
    'name': 'Study Views and Tracking Lesson',
    'version': '1.0',
    'summary': 'Module for studying Odoo Views (Tree, Form) and Field Tracking (Chatter)',
    'category': 'Education',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/readonly_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
