from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about-us.html')