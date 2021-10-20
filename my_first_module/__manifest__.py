# -*- coding: utf-8 -*-
{
    'name': "my_first_module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'queue_job', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/my_first_module_security.xml',
        'views/car_car_views.xml',
        'views/parking_views.xml',
        'views/car_feature_views.xml',
        'views/hr_employee_views.xml',
        'wizard/generate_xlsx_my_car_views.xml',
        'data/ir_cron_job_views.xml',
        'data/sequence.xml',
        'reports/report_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
