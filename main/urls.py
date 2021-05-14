from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

        # Это разделы продаж

    path('plots/', views.plots, name='plots'),
    path('plots/<plots_id>/', views.plots_show, name='plots_id'),
    path('houses/', views.houses, name='houses'),
    path('houses/<houses_id>/', views.houses_show, name='houses_id'),
    path('apartments/', views.apartments, name='apartments'),
    path('apartments/<apartments_id>/', views.apartments_show, name='apartments_id'),
    path('commerce/', views.commerce, name='commerce'),
    path('commerce/<commerce_id>/', views.commerce_show, name='commerce_id'),



    # Это разделы аренд

    path('plots-rent/', views.plots_rent, name='plots_rent'),
    path('plots-rent/<plots_id>/', views.plots_show_rent, name='plots_id_rent'),
    path('houses-rent/', views.houses_rent, name='houses_rent'),
    path('houses-rent/<houses_id>/', views.houses_show_rent, name='houses_id_rent'),
    path('apartments-rent/', views.apartments_rent, name='apartments_rent'),
    path('apartments-rent/<apartments_id>/', views.apartments_show_rent, name='apartments_id_rent'),
    path('commerce-rent/', views.commerce_rent, name='commerce_rent'),
    path('commerce-rent/<commerce_id>/', views.commerce_show_rent, name='commerce_id_rent'),


    path('reviews/', views.reviews, name='reviews'),
    path('reviews/<reviews_id>/', views.reviews_detail, name='reviews_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
