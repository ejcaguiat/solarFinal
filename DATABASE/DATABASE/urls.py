
from django.contrib import admin
from django.urls import path
from SolarDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/salesform/', views.salesregister, name='registerpage'),
    path('homepage/salesview/', views.salesview, name='salesviewpage'),
    path('homepage/leaseview/', views.leaseview, name='leaseviewpage'),
    path('homepage/leaseregister/', views.leaseregister, name='leaseregisterpage'),
    path('homepage/leaseedit/', views.leaseedit, name = 'leaseeditpage'),
    path('homepage/salesedit/', views.salesedit, name = 'saleseditpage'),
    path('homepage/logout/', views.logout, name = 'logout'),
    path('homepage/UNAUTHORIZED_ACCESS/', views.ERROR, name = 'ERROR'),
    path('homepage/salesform/UNAUTHORIZED_ACCESS/', views.ERROR, name = 'ERROR'),
    path('homepage/salesview/UNAUTHORIZED_ACCESS/', views.ERROR, name = 'ERROR'),
    path('homepage/leaseview/UNAUTHORIZED_ACCESS/', views.ERROR, name = 'ERROR'),
    path('homepage/leaseregister/UNAUTHORIZED_ACCESS/', views.ERROR, name = 'ERROR'),
    path('homepage/leaseedit/UNAUTHORIZED_ACCESS/', views.ERROR, name = 'ERROR'),
    path('homepage/salesedit/UNAUTHORIZED_ACCESS/', views.ERROR, name = 'ERROR'),
    
]
