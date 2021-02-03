from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking'),
    path('success/', views.success, name='success'),
    path('inside/',views.inside,name='inside'),
    path('menu/',views.menu,name='menu'),
    path('about/',views.about,name='about'),
    path('reservation/',views.reservation,name='reservation'),
    path('admindashb/',views.admin,name='admindashb'),
    path('shopingcart/',views.shopingcart,name='shopingcart'),
    path('bill/',views.bill,name='bill'),
    path('finalbill/',views.final_bill,name='finalbill'),
    path('admintable/',views.adminPage,name='admintable'),
    path('search/',views.search,name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
