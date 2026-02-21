from django.contrib import admin
from .models import documento

@admin.register(documento)
class documentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'aluno', 'status')
    list_filter = ('status',)