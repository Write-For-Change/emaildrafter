from django.contrib import admin
from .models import EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name")}
