from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    #exclude = ('features',)

admin.site.register(UserApp, UserAdmin)
admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
