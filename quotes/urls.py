from django.urls import path
from . import views
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('add_stock.html', views.add_stock, name="add_stock"),
]
