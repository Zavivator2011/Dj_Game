from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('<str:category>/', home_page, name="category"),
    path('detail/<int:game_id>/', detail_page,name="detail"),
]