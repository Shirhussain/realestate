from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

from .models import Listing, Realtor

def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
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