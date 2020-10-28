from django.contrib import admin

from .models import Listing, Realtor

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','city','is_published','list_date')
    list_display_links = ('title', 'city')
    list_filter = ('realtor','list_date')
    search_fields = ('title','city','state','price','zipcode','description','address')
    list_editable = ('is_published',)
    list_per_page = 30


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','is_mvp')
    list_filter = ('hire_date',)
    search_fields = ('id','name','phone','email')
    list_per_page = 30



admin.site.register(Listing, ListingAdmin)
admin.site.register(Realtor, RealtorAdmin)
