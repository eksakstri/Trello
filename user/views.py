from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def First_view(request, *args, **kwargs):
    #return HttpResponse("<h1>hello world")
    return render(request, "pages/home.html", context={}, status=200)
    
def Detail_view(request, uid, *args, **kwargs):
    obj = user.objects.get(id=uid)
    return HttpResponse(f"<h1>Hello {obj.Username}")
