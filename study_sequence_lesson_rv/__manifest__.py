# {
#     "name": "Study Lesson: Sequences & Create Methodd",
#     "version": "19.0.1.0.0",
#     "category": "Purchases",
#     "summary": "Module to study Sequences",
#     "author": "abc",
#     "license": "LGPL-3",
#     "depends": [
#         "base",
#         "purchase",
#     ],    
#     "data": [
#         "data/ir_sequence_data.xml",
#         "views/purchase_order_view.xml",
#     ],
#     "installable": True,
#     "application": False,
# }

{
    'name': 'Study Lesson: Sequences & Create Method',
    'version': '1.0',
    'category': 'Tutorial',
    'summary': 'Module to study Sequences, Many2one, Rec Name, and Create method overrides in Odoo 19.',
    'depends': ['base', 'purchase'],
    'data': [
        "data/ir_sequence_data.xml",
        "views/purchase_order_view.xml",
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

