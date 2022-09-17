from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ContactMeModel

# Register your models here.

#admin.site.register(Search)


@admin.register(ContactMeModel)
class ContactMeModelAdmin(admin.ModelAdmin):  # customized class
    list_display = ('name', 'email', 'subject', 'message', 'date')
    fieldsets = [
            (None, {'fields': ['name']}),
            ('Date Information', {'fields': ['date'], 'classes': ['collapse']}),
        ]
    list_filter = ['date']  # filter table on the side
    search_fields = ['name', 'email', 'subject', 'message']


