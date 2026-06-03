from django.contrib import admin
from shop.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

    
