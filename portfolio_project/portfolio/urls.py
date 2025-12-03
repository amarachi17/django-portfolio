from django.urls import path 
from . import views
from .views import project_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('project/<int:pk>/', project_detail, name="project_detail"),
]
