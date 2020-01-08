from django.urls import path

from forum import views

app_name = 'forum'

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('forum/all/', views.forum_all, name='all'),
    path('forum/get_comment/<int:pk>', views.get_comment, name='get_comment'),
]
