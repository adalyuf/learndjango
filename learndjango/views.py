from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about-us.html')

def result(request):
    user_input = request.GET['user_input']
    return render(request, 'result.html', {'home_input': user_input} )