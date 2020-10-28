from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

from .models import Listing

def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    return render(request, "realstate/home.html", context)

    
def about(request):
    return render(request, "realstate/about.html", {})


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
    return render(request, "realstate/listing.html", {})