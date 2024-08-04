"""trainingbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('home.urls'), name='home' ),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path("ptsessions/", include('ptsessions.urls'), name='ptsessions' ),
    path("userprograms/", include('userprograms.urls'), name='userprograms' ),
    path("profile_page/", include('profile_page.urls'), name='profile_page' ),
    path("payment/", include('payment.urls'), name='payment_page' ),
    path("basket/", include('basket.urls'), name='basket' ),
    path('admin/', admin.site.urls),
]
