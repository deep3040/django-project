from django.urls import path,include
from .import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.typefetcher,name='type'),
    path('search',views.search,name='search')
    
]