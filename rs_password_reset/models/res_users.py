from odoo import models, _
from odoo.exceptions import ValidationError
import re


def _check_password_strength(password):
    """
    Validate password strength
    Returns: tuple (is_valid, error_message)
    """
    if not password or len(password) < 8:
        return False, _('Password must be at least 8 characters long')

    if not re.search(r'[A-Z]', password):
        return False, _('Password must contain at least one uppercase letter')

    if not re.search(r'[a-z]', password):
        return False, _('Password must contain at least one lowercase letter')

    if not re.search(r'\d', password):
        return False, _('Password must contain at least one digit')

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, _('Password must contain at least one special character (!@#$%^&*(),.?":{}|<>)')

    return True, ''


class ResUsers(models.Model):
    _inherit = 'res.users'

    def write(self, vals):
        """Override write to validate password strength when changing password"""
        if 'password' in vals and vals['password']:
            is_valid, error_msg = _check_password_strength(vals['password'])
            if not is_valid:
                raise ValidationError(error_msg)
        return super(ResUsers, self).write(vals)


    def create(self, vals):
        """Override create to validate password strength when creating user with password"""
        if 'password' in vals and vals['password']:
            is_valid, error_msg = _check_password_strength(vals['password'])
            if not is_valid:
                raise ValidationError(error_msg)
        return super(ResUsers, self).create(vals)
