from django.contrib import admin
from .models import Article, Product, Contact
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('article_slug',)
admin.site.register(Article, ArticleAdmin)

class ProductAdmin(admin.ModelAdmin):
    exclude = ('product_slug',)
admin.site.register(Product, ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['iletisim_isim', 'iletisim_tarihi']

admin.site.register(Contact, ContactAdmin)
