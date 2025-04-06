from django.contrib import admin
from wallet.models import Account, Category, Record

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['user', 'name', 'color', 'category_type']
    fields = list_display
    list_filter = ['user', 'category_type']
    ordering = ['user']


@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    list_display = ['user', 'name']
    fields = ['user', 'name', 'balance']
    list_filter = ['user']
    ordering = ['user', 'balance']


@admin.register(Record)
class AdminRecord(admin.ModelAdmin):
    list_display = ['user', 'description', 'price', 'category', 'created']
    fields = ['user', 'description', 'price', 'category', 'account']
    readonly_fields = ['created']
    list_filter = ['user']
    ordering = ['user', 'price', 'created']