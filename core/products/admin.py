from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product

# Register your models here.

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ['title', 'description']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ("title", )