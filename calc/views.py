from django.shortcuts import render


# from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, "home.html", {'name': 'kishore'})


def add(request):
    """The GET vs POST
    # The GET method takes the input and displays in the address bar (NOT A SECURE WAY)
    # Therefore POST (also change in home.html)
    # Remember to use csrf token in home .html {% csrf_token %}

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    """
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, "result.html", {'result': res})
