from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PtSessions,Price


@admin.register(PtSessions)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('session_name', 'item_price',)
    search_fields = ['session_name']
    list_filter = ('body_part', 'user', 'client')
    summernote_fields = ('program',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff:
            return qs.filter(user=request.user)
        return qs

admin.site.register(Price)