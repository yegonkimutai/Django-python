from django.shortcuts import render

def greet(request):
    x = 1
    y = 3
    return render(request, 'hello.html', {'name': 'Mosh'})
