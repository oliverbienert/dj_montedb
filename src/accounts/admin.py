from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from authtools.admin import UserAdmin as AuthtoolsUserAdmin
from authtools.models import User

# HACK: In user admin detail view, the change password link
# doesn't work. This hack fixes the issue until a fix is
# release.
# https://github.com/fusionbox/django-authtools/issues/91
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(AuthtoolsUserAdmin):
    form = UserChangeForm
