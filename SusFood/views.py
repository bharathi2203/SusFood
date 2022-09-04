from django.shortcuts import render
from .models import Carousel

# Create your views here.
def homeScreenView(request):
    foodCards = Carousel.objects.all()
    print(foodCards)
   
    return render(request, "base.html", {'foodCards' : foodCards})

