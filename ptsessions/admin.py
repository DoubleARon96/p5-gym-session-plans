from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PtSessions, Price


@admin.register(PtSessions)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('session_name', 'item_price',)
    search_fields = ['session_name']
    list_filter = ('body_part', 'user', 'client')
    summernote_fields = ('program',)

    def get_queryset(self, request):
        """
        this function filters if you are staff or not and if you are you can
        only see items and programs that are attached to your user
        """
        admin_content = super().get_queryset(request)
        if request.user.is_staff:
            return admin_content.filter(user=request.user)
        return admin_content


admin.site.register(Price)
