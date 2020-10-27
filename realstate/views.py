from django.shortcuts import render


def home(request):
    return render(request, "realstate/home.html", {})


def about(request):
    return render(request, "realstate/about.html", {})


def homeList(request):
    return render(request, "realstate/listings.html")
    

def homeDetail(request):
    return render(request, "realstate/listing.html", {})