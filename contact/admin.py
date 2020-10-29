from django.contrib import admin
from . models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','phone','date')
    list_display_links = ('id','name')
    search_fields = ('name','email','listing','id')
    list_per_page = 30

admin.site.register(Contact,ContactAdmin)
