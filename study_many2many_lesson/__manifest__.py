{
    'name': 'Study Many2many Lesson',
    'version': '1.0',
    'summary': 'Lesson on Many2many, widget handle, tree editable, and icons',
    'description': 'A module to study Many2many field, web_icon, widget="handle", and tree view editable attributes based on Odoo 17 tutorial.',
    'author': 'Antigravity',
    'category': 'Study',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/lesson_views.xml',
        'views/tag_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
