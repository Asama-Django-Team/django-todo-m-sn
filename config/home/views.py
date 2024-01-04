from django.shortcuts import render, HttpResponse

def intro(request):
    return render(request, 'index.html')
