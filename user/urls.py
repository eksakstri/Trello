from django.urls import path
from . import views

urlpatterns = [
    path('First_view/', views.First_view, name="First_view"),
    path('Detail_view/<int:uid>', views.Detail_view, name="Detail_view"),
]