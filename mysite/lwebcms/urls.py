from django.urls import path
from lwebcms import views

urlpatterns = [
    path('', views.index),
    path('list/', views.list),
    path('artical/<int:id>/', views.artical, name='artical'),
    path('fabu/', views.fabu),
    path('delete/<int:id>/', views.delete_artical, name="artical_delete"),
]