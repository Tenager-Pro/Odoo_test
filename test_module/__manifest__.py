# -*- coding: utf-8 -*-
{
    'name': "test_module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'wizards/test_wizards.xml',
        'views/testPerson.xml',
        'views/testPersonList.xml',
        
    ],

    'demo': [
    ],
}
