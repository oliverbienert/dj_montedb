from django.contrib import admin

from .models import Adult, Child, Income, Address


class IncomeInline(admin.TabularInline):
    
    model = Income
    extra = 0


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    
    pass


@admin.register(Adult)
class AdultAdmin(admin.ModelAdmin):

    inlines = [IncomeInline]


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    
    pass
