from django.conf.urls import include, url
from app5 import views

urlpatterns = [
   
    url(r'^first/', views.first_view),
    url(r'^second/', views.second_view),
    url(r'^third/', views.third_view),
    url(r'^fourth/', views.four_view),
    url(r'^fifth/', views.fifth_view),

]
