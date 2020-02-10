from django.contrib import admin

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

    class Media:
        js = (
            "/static/jquery/js/i18n/datepicker-de.js",
            "/static/site/js/changeyear.js",
        )

    inlines = (IncomeInline, PhoneNumberInline, EmailAddressInline, AdultChildInline, )


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):

    class Media:
        js = (
            "/static/jquery/js/i18n/datepicker-de.js",
            "/static/site/js/changeyear.js",
        )

    inlines = (AdultChildInline, RulingInline, )
