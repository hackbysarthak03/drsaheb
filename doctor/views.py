from django.shortcuts import render

# Create your views here.
def ourHeroes(request):
    return render(request, 'OurHeroes.html')
