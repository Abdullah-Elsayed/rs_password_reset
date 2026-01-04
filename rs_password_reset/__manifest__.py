# -*- coding: utf-8 -*-
{
    'name': "Password Reset",

    'summary': """
        Password Reset by link via copy paste
    """,

    'description': """
        This module allows users to reset their passwords by copying and pasting a link.
        password strength, password reset link, user authentication, account security, user management, password recovery
    """,

    'author': "Abdullah El-sayed",
    'license': 'LGPL-3',
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'auth_signup'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/reset_password_wizard_view.xml',
        'views/res_users_view.xml',
        'views/reset_password_template.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'rs_password_reset/static/src/js/password_strength.js',
            'rs_password_reset/static/src/css/password_strength.css',
        ],
    },
    'installable': True,
}
