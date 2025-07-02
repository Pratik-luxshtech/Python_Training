from django.http import HttpResponse

def hello_api(request):
    return HttpResponse("Hello, This is my first Django API response.")
