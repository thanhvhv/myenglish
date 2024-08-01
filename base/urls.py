from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('study/<str:pk>/', views.study, name='study'),
    path('review/<str:pk>/', views.review, name='review'),
    path('update_word/', views.update_word, name='update_word'),

]