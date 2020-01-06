from django.urls import path

from resources import views

app_name = 'resources'

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.questions, name='questions'),
    path('resources/', views.resources, name='resources'),
    path('resources/books/', views.books, name='books'),
    path('resources/sources', views.sources, name='sources'),
    path('resources/products', views.products, name='products'),
    path('about/', views.about, name='about'),
]
