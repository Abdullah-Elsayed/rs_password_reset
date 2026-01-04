from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResetPasswordWizard(models.TransientModel):
    _name = 'reset.password.wizard'
    _description = 'Reset Password Wizard (No Email)'

    user_id = fields.Many2one(
        'res.users',
        string="User",
        required=True
    )

    reset_link = fields.Char(
        string="Reset Password Link",
        readonly=True
    )

    def action_generate_link(self):
        """Generates a password reset link for the selected user without sending an email."""
        if not self.user_id:
            raise ValidationError("Please select a user to generate the reset link.")

        self.user_id.mapped('partner_id').signup_prepare(signup_type="reset")
        self.reset_link = self.user_id.signup_url
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reset Password Link',
            'res_model': 'reset.password.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }
