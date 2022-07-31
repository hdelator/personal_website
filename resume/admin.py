from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ContactMeForm

# Register your models here.

#admin.site.register(Search)


@admin.register(ContactMeForm)
class ContactMeFormAdmin(admin.ModelAdmin):  # customized class
    list_display = ('name', 'email', 'subject', 'message', 'date')
    fieldsets = [
            (None, {'fields': ['name']}),
            ('Date Information', {'fields': ['date'], 'classes': ['collapse']}),
        ]
    list_filter = ['date']  # filter table on the side
    search_fields = ['name', 'email', 'subject', 'message']


