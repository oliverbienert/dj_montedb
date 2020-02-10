from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(label=_('Remember me'), required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field("username", placeholder=_("Enter Email"), autofocus=""),
            Field("password", placeholder=_("Enter Password")),
            HTML(
                '<a href="{}">{}</a>'.format(reverse("accounts:password-reset"), _('Forgot Password?'))
            ),
            Field("remember_me", placeholder=_("Remember Me")),
            Submit("sign_in", _("Log in"), css_class="btn btn-lg btn-primary btn-block"),
        )


class SignupForm(authtoolsforms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field("email", placeholder=_("Enter Email"), autofocus=""),
            Field("name", placeholder=_("Enter Full Name")),
            Field("password1", placeholder=_("Enter Password")),
            Field("password2", placeholder=_("Re-enter Password")),
            Submit("sign_up", _("Sign up"), css_class="btn-warning"),
        )


class PasswordChangeForm(authforms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("old_password", placeholder=_("Enter old password"), autofocus=""),
            Field("new_password1", placeholder=_("Enter new password")),
            Field("new_password2", placeholder=_("Enter new password (again)")),
            Submit("pass_change", _("Change Password"), css_class="btn-warning"),
        )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("email", placeholder=_("Enter email"), autofocus=""),
            Submit("pass_reset", _("Reset Password"), css_class="btn-warning"),
        )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("new_password1", placeholder=_("Enter new password"), autofocus=""),
            Field("new_password2", placeholder=_("Enter new password (again)")),
            Submit("pass_change", _("Change Password"), css_class="btn-warning"),
        )
