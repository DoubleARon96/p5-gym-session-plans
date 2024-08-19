from django.urls import path
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('home.urls'), name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path("ptsessions/", include('ptsessions.urls'), name='ptsessions'),
    path("userprograms/", include('userprograms.urls'), name='userprograms'),
    path("profile_page/", include('profile_page.urls'), name='profile_page'),
    path("payment/", include('payment.urls'), name='payment_page'),
    path("basket/", include('basket.urls'), name='basket'),
    path('admin/', admin.site.urls),
]
