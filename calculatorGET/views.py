from django.shortcuts import render

# Create your views here.
def home(request, equation = "notthing!"):
    result = "unknow"
    if len(equation.split('+')) > 1:
        eqnList = equation.split('+')
        x = float(eqnList[0]) 
        y = float(eqnList[1])
        result = x + y
    elif len(equation.split('-')) > 1:
        eqnList = equation.split('-')
        x = float(eqnList[0]) 
        y = float(eqnList[1])
        result = x - y
    elif len(equation.split('*')) > 1:
        eqnList = equation.split('*')
        x = float(eqnList[0]) 
        y = float(eqnList[1])
        result = x * y
    elif len(equation.split('%')) > 1:
        eqnList = equation.split('%')
        x = float(eqnList[0]) 
        y = float(eqnList[1])
        result = x / y
    return render(request, "homeGET.html", {'equation':equation, 'result':result})

def aboutme(request):
    return render(request, "aboutme.html")

def index(request):
    return render(request, "index.html")