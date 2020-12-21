from django.http import HttpResponse

def about_us(request):
    return HttpResponse("This site built by Alex Daly as a project for learning Django and Docker")

def temporary_homepage(request):
    return HttpResponse("This is a temporary homepage")