from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['reporter', 'reported', 'reason', 'timestamp']
    search_fields = ['reporter__email', 'reported__email', 'reason']


# Register your models here.
