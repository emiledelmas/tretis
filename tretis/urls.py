"""tretis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mainapp import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django_email_verification import urls as mail_urls
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.tretis, name='home'),
    path('br/', views.tretisBR, name='br'),
    path('pr/', views.tretisPR, name='pr'),

    path('register/', views.register, name='register'),
    path('accounts/social/signup/', views.email_already_exist, name="account_email"),
    path('profile/', views.profile_page, name="profile_page"),
    path('new_home/',views.new_home, name="new_home"),
    path('history/<slug:username>',views.history),
    path('leaderboard/',views.global_leaderboard),
    path('', include('django.contrib.auth.urls')),
    path('accounts/',include('allauth.urls')),
]
