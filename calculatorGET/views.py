from django.shortcuts import render

# Create your views here.
def home(request, equation = 0):
    return render(request, "homeGET.html")