{
    'name': "Password Strength Meter and Reset by Link",

    'summary': """
        This module provides a password strength meter and allows users to reset their passwords by copying and pasting a link.
    """,

    'description': """
Password Strength Meter and Reset by Link
==============================================
This Odoo module enhances the password reset process by providing a real-time password strength meter and allowing users to reset their passwords via a copy-paste link. It ensures that users create strong passwords by giving visual feedback and enforcing password requirements.
Features:
---------
* Real-time password strength meter
* Visual feedback with color-coded indicators
* Interactive requirements checklist
* Password match validation
* Prevents submission of weak passwords
* User-friendly interface
* Reset password via copy-paste link
* No email sending required for password reset
* Secure password reset process

Password Requirements:
----------------------
* Minimum 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one digit
* At least one special character
Installation:
-------------
1. Download the module and place it in your Odoo addons directory.
2. Update the apps list in Odoo.
3. Install the "Password Strength Meter and Reset by Link" module.
Usage:
------
1. Navigate to the password reset page.
2. Enter your new password and observe the strength meter.
3. Copy the generated reset link and paste it into your browser to reset your password. 

        
    """,

    'author': "Abdullah El-sayed",
    'website': "abdullahelsaayed@outlook.com",
    'category': 'Tools',
    'version': '0.1',

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

    'images': [
        'static/description/icon.png',
        'static/description/screenshots/screenshot1.png',
        'static/description/screenshots/screenshot2.png',
        'static/description/screenshots/screenshot3.png',
        'static/description/screenshots/screenshot4.png',
        'static/description/screenshots/screenshot5.png',
        'static/description/screenshots/screenshot6.png',

    ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',

    'price': 0.0,
    'currency': 'USD',
}
