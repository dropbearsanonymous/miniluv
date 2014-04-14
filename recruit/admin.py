from django.contrib import admin
from recruit.models import Account, EveAccount, Character

#  Register your models here.

class EveAccountInline(admin.StackedInline):
    model = EveAccount
    extra = 1

class AccountAdmin(admin.ModelAdmin):
    inlines = [EveAccountInline]

admin.site.register(Account, AccountAdmin)
