from django.shortcuts import render

# Create your views here.
def homeScreenView(request):
    print(request.headers)
    return render(request, "base.html", {})