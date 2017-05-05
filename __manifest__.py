# -*- coding: utf-8 -*-
{
    'name': "akademik",

    'summary': """
        Sistim Informasi AKADEMIK""",

    'description': """
        Modul belajar odoo BK3D
    """,

    'author': "Dota Karo",
    'website': "http://www.dotakaro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1-alpha',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/kursus.xml',
        'views/session.xml',
        'views/peserta.xml',
        'views/pengajar.xml',
        'views/peserta_inherit.xml',
        'views/views.xml',
        'views/templates.xml',
        'reports/session_rpt.xml',
        'reports/kursus_rpt.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}