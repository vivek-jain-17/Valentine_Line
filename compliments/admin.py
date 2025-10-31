from django.contrib import admin
from .models import Compliment, SharedCompliment

@admin.register(Compliment)
class ComplimentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'share_count')
    search_fields = ('text',)
    readonly_fields = ('created_at',)

@admin.register(SharedCompliment)
class SharedComplimentAdmin(admin.ModelAdmin):
    list_display = ('compliment', 'created_at')
    readonly_fields = ('created_at',)