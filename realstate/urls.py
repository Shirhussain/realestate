from django.urls import path
from .views import home, about, homeList


app_name = "realstate"
urlpatterns = [
    path('', home, name = "home"),
    path('about', about, name = "about"),
    path('list', homeList, name = "home_list"),
]
