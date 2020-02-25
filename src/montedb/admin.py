from django.contrib import admin
from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.translation import ugettext_lazy as _


from .models import Adult, Child, Income, Address, PhoneNumber, EmailAddress, AdultChild, Ruling


class MonteDbTabularInline(admin.TabularInline):

    extra = 0


class IncomeInline(MonteDbTabularInline):
    
    model = Income


class PhoneNumberInline(MonteDbTabularInline):

    model = PhoneNumber


class EmailAddressInline(MonteDbTabularInline):

    model = EmailAddress


class AdultChildInline(MonteDbTabularInline):

    model = AdultChild


class RulingInline(MonteDbTabularInline):

    model = Ruling


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return False


@admin.register(Adult)
class AdultAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'address', 'phone_private', 'phone_work', 'phone_mobile',
                    'email_private', 'email_work')

    class Media:
        js = (
            "/static/jquery/js/i18n/datepicker-de.js",
            "/static/site/js/changeyear.js",
        )

    inlines = (IncomeInline, PhoneNumberInline, EmailAddressInline, AdultChildInline, )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    full_name.short_description = _('Full name')
    full_name.admin_order_field = Concat('first_name', Value(' '), 'last_name')

    def phone_private(self, obj):
        lst = [item.phone_number.as_international for item in obj.phonenumber_set.filter(type__exact='private')]
        return ", ".join(lst)

    phone_private.short_description = _("Private")

    def phone_work(self, obj):
        lst = [item.phone_number.as_international for item in obj.phonenumber_set.filter(type__exact='work')]
        return ", ".join(lst)

    phone_work.short_description = _("Work")

    def phone_mobile(self, obj):
        lst = [item.phone_number.as_international for item in obj.phonenumber_set.filter(type__exact='mobile')]
        return ", ".join(lst)

    phone_mobile.short_description = _("Mobile")

    def email_private(self, obj):
        lst = [item.email_address for item in obj.emailaddress_set.filter(type__exact='private')]
        return ", ".join(lst)

    email_private.short_description = _("E-Mail (Private)")

    def email_work(self, obj):
        lst = [item.email_address for item in obj.emailaddress_set.filter(type__exact='work')]
        return ", ".join(lst)

    email_work.short_description = _("E-Mail (Work)")


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.DateField: {'required': True}
    }

    list_display = ('full_name', 'care_time', 'age')

    class Media:
        js = (
            "/static/jquery/js/i18n/datepicker-de.js",
            "/static/site/js/changeyear.js",
        )

    inlines = (AdultChildInline, RulingInline, )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    full_name.short_description = _('Full name')
    full_name.admin_order_field = Concat('first_name', Value(' '), 'last_name')
