"""
URL configuration for restaurant_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.views import contact_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/', user_views.signup, name='signup'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('menu/', user_views.menu, name='menu'),
    path('', user_views.home, name='home'),
    path('order_summary', user_views.order_summary, name='order_summary'),
    path('confirmation', user_views.confirmation, name='confirmation'),
    path('profile/', user_views.profile, name='profile'), 
    path('contact/', contact_view, name='contact'),
]
