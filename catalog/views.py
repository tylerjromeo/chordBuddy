from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'title': 'home'
    }
    return render(request, 'catalog/home.html', context)
