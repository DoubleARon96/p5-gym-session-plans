from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PtSessions,Price


@admin.register(PtSessions)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('session_name', 'item_price',)
    search_fields = ['session_name']
    list_filter = ('body_part','user','client')
    summernote_fields = ('program',)
    

admin.site.register(Price)