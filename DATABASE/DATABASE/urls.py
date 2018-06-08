
from django.contrib import admin
from django.urls import path
from SolarDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/salesform/', views.salesregister, name='registerpage'),
    path('homepage/salesview/', views.salesview, name='salesviewpage'),
    path('homepage/leaseview/', views.leaseview, name='leaseviewpage'),
    path('homepage/leaseregister/', views.leaseregister, name='leaseregisterpage'),
    
]
