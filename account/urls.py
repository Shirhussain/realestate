from django.urls import path
from .views import login, dashboard, logout, register


app_name = "account"
urlpatterns = [
    path('login/', login, name = "login"),
    path('register/', register, name = "register"),
    path('logout/', logout, name = "logout"),
    path('dashboard/', dashboard, name = "dashboard"),
]

