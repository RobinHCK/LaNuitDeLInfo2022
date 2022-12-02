from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipe/', views.equipe, name='equipe'),
    path('generation_logo/', views.generation_logo, name='generation_logo'),
    path('data_story/', views.data_story, name='data_story'),
]
