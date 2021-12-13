from django.contrib import admin
from .models import Product, Images, Beads

class ImageAdmin(admin.StackedInline):
    model = Images

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ['name', 'price', 'desc']
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
       model = Product

@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Beads)
class BeadAdmin(admin.ModelAdmin):
    list_display = ['name','price']
