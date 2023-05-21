from django.urls import path
from AppUrlTemp import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]     
