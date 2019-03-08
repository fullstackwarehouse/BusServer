from django.contrib import admin
from .models import Department, Site, Line, Line2Site, Bus, Bus2Line

# Register your models here.
admin.site.register(Department)
admin.site.register(Site)
admin.site.register(Line)
admin.site.register(Line2Site)
admin.site.register(Bus)
admin.site.register(Bus2Line)
