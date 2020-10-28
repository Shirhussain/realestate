from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

from .models import Listing, Realtor
from . choices import state_choices, bedroom_choices, price_choices

def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]


    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }
    return render(request, "realstate/home.html", context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    #get seller of the month 
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, "realstate/about.html", context)


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'listings': page_obj,
    }
    return render(request, "realstate/listings.html", context)
    

def homeDetail(request, list_id):
    list = get_object_or_404(Listing, pk=list_id)

    context = {
        'list': list
    }
    return render(request, "realstate/listing.html", context)


def search(request):
    query_list = Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords: 
            query_list = query_list.filter(description__icontains=keywords)

    #city 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
    

    #state
    #for state be careful that everything you get as input should be you key in dictionary 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)


    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)
    
    #price 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': query_list
    }
    return render(request, "realstate/search.html", context)