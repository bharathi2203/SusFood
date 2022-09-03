from django.shortcuts import render
from .models import Carousel

# Create your views here.
def homeScreenView(request):
    obj = Carousel.objects.all()
    context ={
        'obj' : obj
    }
    return render(request, "base.html", context)