from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from rest_framework import viewsets,permissions

from .models import users, projects, lists, cards
from .serializers import userserializer, projectserializer, listserializer, cardserializer
from .permissions import IsAdmin, IsMember

# Create your views here.

"""def First_view(request, *args, **kwargs):
    #return HttpResponse("<h1>hello world")
    return render(request, "pages/home.html", context={}, status=200)
    
def Detail_view(request, uid, *args, **kwargs):
    obj = user.objects.get(id=uid)
    return HttpResponse(f"<h1>Hello {obj.Username}")"""

class UserViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = userserializer
    permission_classes = [IsAdmin, permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = projects.objects.all()
    serializer_class = projectserializer
    permission_classes = [IsAdmin, IsMember, permissions.IsAuthenticated]

class ListViewSet(viewsets.ModelViewSet):
    queryset = lists.objects.all()
    serializer_class = listserializer
    permission_classes = [IsAdmin, IsMember, permissions.IsAuthenticated]

class CardViewSet(viewsets.ModelViewSet):
    queryset = cards.objects.all()
    serializer_class = cardserializer
    permission_classes = [IsAdmin, IsMember, permissions.IsAuthenticated]


