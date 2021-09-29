from django.urls import path
from . import views

urlpatterns = [
    path('', views.First_view, name="First_view"),
    path('Detail_view/<int:uid>', views.Detail_view, name="Detail_view"),
]