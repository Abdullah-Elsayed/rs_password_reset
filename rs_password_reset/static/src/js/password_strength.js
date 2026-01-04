odoo.define('password_strength.reset_password', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.PasswordStrength = publicWidget.Widget.extend({
    selector: '.oe_signup_form, .oe_reset_password_form',
    events: {
        'keyup input[id="password"]': '_onPasswordChange',
        'keyup input[name="password"]': '_onPasswordChange',
        'keyup input[id="confirm_password"]': '_onConfirmPasswordChange',
        'keyup input[name="confirm_password"]': '_onConfirmPasswordChange',
    },

    start: function () {
        this._super.apply(this, arguments);
        // Disable submit button on page load
        this._disableSubmitButton();
    },

    _onPasswordChange: function (ev) {
        var password = $(ev.currentTarget).val();
        this._checkPasswordStrength(password);
        this._checkPasswordMatch();
    },

    _onConfirmPasswordChange: function (ev) {
        this._checkPasswordMatch();
    },

    _checkPasswordMatch: function () {
        var password = this.$el.find('input[id="password"], input[name="password"]').val();
        var confirmPassword = this.$el.find('input[id="confirm_password"], input[name="confirm_password"]').val();
        var matchIndicator = this.$el.find('#password-match-indicator');
        var matchMessage = this.$el.find('#match-message');

        // Only show match indicator if confirm password field has content
        if (confirmPassword.length > 0) {
            matchIndicator.show();

            if (password === confirmPassword) {
                matchMessage.html('<i class="fa fa-check-circle"></i> Passwords match');
                matchMessage.removeClass('text-danger').addClass('text-success');
            } else {
                matchMessage.html('<i class="fa fa-times-circle"></i> Passwords do not match');
                matchMessage.removeClass('text-success').addClass('text-danger');
            }
        } else {
            matchIndicator.hide();
        }

        // Update button state
        this._updateSubmitButton();
    },

    _checkPasswordStrength: function (password) {
        var strength = 0;
        var strengthText = '';
        var strengthClass = '';

        // Check requirements
        var hasLength = password.length >= 8;
        var hasUpper = /[A-Z]/.test(password);
        var hasLower = /[a-z]/.test(password);
        var hasNumber = /\d/.test(password);
        var hasSpecial = /[!@#$%^&*(),.?":{}|<>]/.test(password);

        // Update requirement indicators
        this._updateRequirement('req-length', hasLength);
        this._updateRequirement('req-upper', hasUpper);
        this._updateRequirement('req-lower', hasLower);
        this._updateRequirement('req-number', hasNumber);
        this._updateRequirement('req-special', hasSpecial);

        // Calculate strength
        if (hasLength) strength++;
        if (hasUpper) strength++;
        if (hasLower) strength++;
        if (hasNumber) strength++;
        if (hasSpecial) strength++;

        // Update strength bar
        var strengthBar = this.$el.find('#strength-bar');
        var strengthTextEl = this.$el.find('#strength-text');

        if (password.length === 0) {
            strengthBar.css('width', '0%');
            strengthTextEl.text('');
            this._disableSubmitButton();
            return;
        }

        switch (strength) {
            case 1:
            case 2:
                strengthClass = 'weak';
                strengthText = 'Weak';
                strengthBar.css('width', '33%');
                break;
            case 3:
            case 4:
                strengthClass = 'medium';
                strengthText = 'Medium';
                strengthBar.css('width', '66%');
                break;
            case 5:
                strengthClass = 'strong';
                strengthText = 'Strong';
                strengthBar.css('width', '100%');
                break;
        }

        strengthBar.removeClass('weak medium strong').addClass(strengthClass);
        strengthTextEl.text(strengthText).removeClass('weak medium strong').addClass(strengthClass);

        // Update button state
        this._updateSubmitButton();
    },

    _updateRequirement: function (reqId, met) {
        var reqEl = this.$el.find('#' + reqId);
        if (met) {
            reqEl.find('i').removeClass('fa-circle-o').addClass('fa-check-circle text-success');
            reqEl.addClass('text-success');
        } else {
            reqEl.find('i').removeClass('fa-check-circle text-success').addClass('fa-circle-o');
            reqEl.removeClass('text-success');
        }
    },

    _updateSubmitButton: function () {
        var password = this.$el.find('input[id="password"], input[name="password"]').val();
        var confirmPassword = this.$el.find('input[id="confirm_password"], input[name="confirm_password"]').val();

        // Check if password meets all requirements
        var hasLength = password.length >= 8;
        var hasUpper = /[A-Z]/.test(password);
        var hasLower = /[a-z]/.test(password);
        var hasNumber = /\d/.test(password);
        var hasSpecial = /[!@#$%^&*(),.?":{}|<>]/.test(password);
        var allRequirementsMet = hasLength && hasUpper && hasLower && hasNumber && hasSpecial;

        // Check if passwords match
        var passwordsMatch = password === confirmPassword && confirmPassword.length > 0;

        // Enable button only if all requirements are met AND passwords match
        if (allRequirementsMet && passwordsMatch) {
            this._enableSubmitButton();
        } else {
            this._disableSubmitButton();
        }
    },

    _disableSubmitButton: function () {
        var submitBtn = this.$el.find('button[type="submit"]');
        submitBtn.prop('disabled', true);
        submitBtn.addClass('btn-disabled');
    },

    _enableSubmitButton: function () {
        var submitBtn = this.$el.find('button[type="submit"]');
        submitBtn.prop('disabled', false);
        submitBtn.removeClass('btn-disabled');
    },
});

return publicWidget.registry.PasswordStrength;
});

