from django.contrib import admin
from .models import Volunteers, Branch
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Volunteers, AuthorAdmin)
admin.site.register(Branch, AuthorAdmin)
