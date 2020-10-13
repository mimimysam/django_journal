from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('update/<str:pk>', views.editEntry, name='update'),
    path('delete/<str:pk>', views.deleteEntry, name='delete'),
    path('search/', views.search, name='search')
]
