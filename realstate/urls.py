from django.urls import path
from .views import home, about, listings, homeDetail, search


app_name = "realstate"
urlpatterns = [
    path('', home, name = "home"),
    path('about/', about, name = "about"),
    path('list/', listings, name = "home_list"),
    path('search/', search, name = "search"),
    path('detail/<int:list_id>/', homeDetail, name = "home_detail"),
]

