
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
    path('homepage/salesedit/edit_sales_form', views.editSform, name = 'edit_sales_form')
]
