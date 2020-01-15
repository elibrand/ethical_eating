from django.urls import path

from resources import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'resources'

urlpatterns = [
    path('', views.index, name='index'),
    path('why', views.why, name='why'),
    path('questions/', views.questions, name='questions'),
    path('resources/', views.resources, name='resources'),
    path('resources/books/', views.books, name='books'),
    path('resources/food/', views.food, name='food'),
    path('resources/food/reviews/<int:pk>', views.reviews, name='reviews'),
    path('resources/products/', views.products, name='products'),
    path('resources/sources/bible', views.bible, name='bible'),
    path('resources/sources/talmud', views.talmud, name='talmud'),
    path('resources/sources/rabbis', views.rabbis, name='rabbis'),
    path('resources/sources/thinkers', views.thinkers, name='thinkers'),
    path('about/', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
