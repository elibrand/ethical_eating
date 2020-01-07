from django.urls import path

from resources import views

app_name = 'resources'

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.questions, name='questions'),
    path('resources/', views.resources, name='resources'),
    path('resources/books/', views.books, name='books'),
    path('resources/products/', views.products, name='products'),
    path('resources/sources/', views.sources, name='sources'),
    path('resources/sources/bible', views.bible, name='bible'),
    path('resources/sources/talmud', views.talmud, name='talmud'),
    path('resources/sources/rabbis', views.rabbis, name='rabbis'),
    path('resources/sources/thinkers', views.thinkers, name='thinkers'),
    path('about/', views.about, name='about'),
    path('perv/', views.perv, name='perv'),
]
