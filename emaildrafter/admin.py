from django.contrib import admin
from .models import EmailTemplate, SpecificTarget, MP, Topic, EmailTemplateSubmitter


class EmailTemplateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(SpecificTarget)
admin.site.register(Topic)
admin.site.register(MP)
admin.site.register(EmailTemplateSubmitter)
