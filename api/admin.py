from django.contrib import admin
from api.models import Person


# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sections')


class PersonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fl_name', 'rooms', 'phone', 'internal_address', 'section')


admin.site.register(Person, PersonsAdmin)

