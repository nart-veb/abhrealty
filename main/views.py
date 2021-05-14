from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from itertools import chain
from .models import *



def index(request):
    typesapartments = TypesApartments.objects.all()
    cities = Cities.objects.all()
    typesale = Typesale.objects.all()
    apartments_block = Apartments.objects.filter(announcement__vip=2)
    houses_block = Houses.objects.filter(announcement__vip=2)
    plots_block = Plots.objects.filter(announcement__vip=2)
    commerce_block = Commerce.objects.filter(announcement__vip=2)
    block_el = list(chain(apartments_block, houses_block, plots_block, commerce_block))
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/home.html', {'title': 'Главная','typesapartments': typesapartments, 'cities':cities, 'typesale':typesale, 'block_el':block_el,  'projectImage': projectImage})

def about(request):
    return render(request, 'main/about.html')


# Раздел продажа
def plots(request):
    plots = Plots.objects.filter(announcement__typesale='1').order_by('-id')
    # plots = Plots.objects.order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/plots/plots.html', {'title': 'Участки', 'plots': plots,  'projectImage': projectImage})

def plots_show(request, plots_id):
    # plots_block_price = Plots.objects.filter(~Q(id=plots_id)).order_by('announcement__price')
    plots_block_price = Plots.objects.filter(~Q(id=plots_id)).order_by('announcement__price')
    plots_block_price = plots_block_price.filter(announcement__typesale='1')
    plots = get_object_or_404(Plots, id=plots_id)
    plots_title = plots.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/plots/plots-detail.html', {'title': plots_title, 'plots':plots, 'projectImage': projectImage, 'plots_block_price':plots_block_price})


def houses(request):
    houses = Houses.objects.filter(announcement__typesale='1').order_by('-id')
    # houses = Houses.objects.order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/houses/houses.html', {'title': 'Дома', 'houses': houses,  'projectImage': projectImage})

def houses_show(request, houses_id):
    houses_block_price = Houses.objects.filter(~Q(id=houses_id)).order_by('announcement__price')
    houses_block_price = houses_block_price.filter(announcement__typesale='1')
    houses = get_object_or_404(Houses, id=houses_id)
    houses_title = houses.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/houses/houses-detail.html', {'title': houses_title, 'houses':houses, 'projectImage': projectImage, 'houses_block_price':houses_block_price})



def apartments(request):
    apartments = Apartments.objects.filter(announcement__typesale='1').order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/apartments/apartaments.html', {'title': 'Квартиры', 'apartments': apartments,  'projectImage': projectImage})

def apartments_show(request, apartments_id):
    apartments_block_price = Apartments.objects.filter(~Q(id=apartments_id)).order_by('announcement__price')
    apartments_block_price = apartments_block_price.filter(announcement__typesale='1')
    apartments = get_object_or_404(Apartments, id=apartments_id)
    apartments_title = apartments.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/apartments/apartments-detail.html', {'title': apartments_title, 'apartments':apartments, 'projectImage': projectImage, 'apartments_block_price':apartments_block_price})


def commerce(request):
    commerce = Commerce.objects.filter(announcement__typesale='1').order_by('-id')
    # commerce = Commerce.objects.order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/commerce/commerce.html', {'title': 'Коммерческая недвижимость', 'commerce': commerce,  'projectImage': projectImage})

def commerce_show(request, commerce_id):
    commerce_block_price = Commerce.objects.filter(~Q(id=commerce_id)).order_by('announcement__price')
    commerce_block_price = commerce_block_price.filter(announcement__typesale='1')
    commerce = get_object_or_404(Commerce, id=commerce_id)
    commerce_title = commerce.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/commerce/commerce-detail.html', {'title': commerce_title, 'commerce':commerce, 'projectImage': projectImage, 'commerce_block_price':commerce_block_price})












# Раздел аренда
def plots_rent(request):
    plots = Plots.objects.filter(announcement__typesale='2').order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/plots/plots.html', {'title': 'Участки', 'plots': plots,  'projectImage': projectImage})

def plots_show_rent(request, plots_id):
    plots_block_price = Plots.objects.filter(~Q(id=plots_id)).order_by('announcement__price')
    plots_block_price = plots_block_price.filter(announcement__typesale='2')
    plots = get_object_or_404(Plots, id=plots_id)
    plots_title = plots.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/plots/plots-detail.html', {'title': plots_title, 'plots':plots, 'projectImage': projectImage, 'plots_block_price':plots_block_price})


def houses_rent(request):
    houses = Houses.objects.filter(announcement__typesale='2').order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/houses/houses.html', {'title': 'Дома', 'houses': houses,  'projectImage': projectImage})

def houses_show_rent(request, houses_id):
    # houses_block_price = Houses.objects.filter(~Q(id=houses_id)).order_by('announcement__price')
    houses_block_price = Houses.objects.filter(~Q(id=houses_id)).order_by('announcement__price')
    houses_block_price = houses_block_price.filter(announcement__typesale='2')
    houses = get_object_or_404(Houses, id=houses_id)
    houses_title = houses.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/houses/houses-detail.html', {'title': houses_title, 'houses':houses, 'projectImage': projectImage, 'houses_block_price':houses_block_price})



def apartments_rent(request):
    apartments = Apartments.objects.filter(announcement__typesale='2').order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/apartments/apartaments.html', {'title': 'Квартиры', 'apartments': apartments,  'projectImage': projectImage})

def apartments_show_rent(request, apartments_id):
    # apartments_block_price = Apartments.objects.filter(~Q(id=apartments_id)).order_by('announcement__price')
    apartments_block_price = Apartments.objects.filter(~Q(id=apartments_id)).order_by('announcement__price')
    apartments_block_price = apartments_block_price.filter(announcement__typesale='2')
    apartments = get_object_or_404(Apartments, id=apartments_id)
    apartments_title = apartments.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/apartments/apartments-detail.html', {'title': apartments_title, 'apartments':apartments, 'projectImage': projectImage, 'apartments_block_price':apartments_block_price})


def commerce_rent(request):
    commerce = Commerce.objects.filter(announcement__typesale='2').order_by('-id')
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/commerce/commerce.html', {'title': 'Коммерческая недвижимость', 'commerce': commerce,  'projectImage': projectImage})

def commerce_show_rent(request, commerce_id):
    # commerce_block_price = Commerce.objects.filter(~Q(id=commerce_id)).order_by('announcement__price')
    commerce_block_price = Commerce.objects.filter(~Q(id=commerce_id)).order_by('announcement__price')
    commerce_block_price = commerce_block_price.filter(announcement__typesale='2')
    commerce = get_object_or_404(Commerce, id=commerce_id)
    commerce_title = commerce.name
    projectImage = ProjectImage.objects.all()
    return render(request, 'main/commerce/commerce-detail.html', {'title': commerce_title, 'commerce':commerce, 'projectImage': projectImage, 'commerce_block_price':commerce_block_price})




def reviews(request):
    reviews = Reviews.objects.all().order_by('-date')
    return render(request, 'main/reviews/reviews.html', {'title': 'Отзывы о нас' , 'reviews': reviews})

def reviews_detail(request, reviews_id):
    reviews = get_object_or_404(Reviews, id=reviews_id)
    return render(request, 'main/reviews/reviews-detail.html', {'title': 'Отзывы о нас' , 'reviews': reviews})
