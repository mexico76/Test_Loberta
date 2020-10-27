from django.contrib import admin
from .models import TestLink

class TestLinkAdmin(admin.ModelAdmin):
    list_display = ['link',]

admin.site.register(TestLink, TestLinkAdmin)
