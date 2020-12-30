"""mini_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from fest_app import views
from django.conf.urls.static import static
urlpatterns = [

    path('', views.home, name="home"),
    path('admin/', admin.site.urls, name='admin'),
    path('register/<int:id>/', views.register, name='register'),
    path('createevent/', views.CreateEvent, name='event'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('jury/', views.CreateJury, name='jury'),
    path('visitor/<int:id>/', views.Visitor, name='visitor'),
    path('update/<int:id>/', views.Update, name='update'),
    path('delete/<int:id>/', views.DeleteEvent, name='delete'),
    path('list/', views.EventList, name='event_list')


    # path('register/', views.vol_form, name="register"),
    # path('table/', views.display_table, name="table")
]
