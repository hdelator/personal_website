from django.contrib import admin
from .models import ContactMeModel
from django.contrib.auth.models import Group

admin.site.unregister(Group) # removes the group icon, not used

# Register your models here.

@admin.register(ContactMeModel)
class PostAdmin(admin.ModelAdmin):  # customized class
    list_display = ('name', 'email', 'subject', 'message', 'created')
    fieldsets = [
            (None, {'fields': ['name']}),
            ('Date Information', {'fields': ['created'], 'classes': ['collapse']}),
        ]
    list_filter = ['created']  # filter table on the side
    search_fields = ['name', 'email', 'subject']


