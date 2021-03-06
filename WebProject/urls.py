"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # admin url
    path('admin/', admin.site.urls),
    #
    path('rejestracja/', user_views.register, name="register"),
    path('logowanie/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('wylogowywanie/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('reset/zrobiony/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('reset/powierdzanie/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/zakończony/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
    # homepage url
    path('', include('memopolis.urls')),
    #
    path('profil/', user_views.profile, name="profile"),
    
    #API
    path('api-auth/', include('rest_framework.urls')),
    path('api/memopolis/', include('memopolis.api.urls')),
    path('api/users/', include('users.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)