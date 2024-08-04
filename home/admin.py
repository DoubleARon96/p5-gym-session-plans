from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import HomeNews


@admin.register(HomeNews)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('user','updated_on')
    search_fields = ['session_name']
    list_filter = ('user',)
    summernote_fields = ('content','title')