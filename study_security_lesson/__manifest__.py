{
    'name': 'Study Security Lesson',
    'version': '1.0',
    'summary': 'Module for studying Odoo Security (Groups, Access Rights, Record Rules)',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
