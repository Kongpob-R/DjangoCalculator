from django.shortcuts import render

# Create your views here.
def home(request):
    result = 0
    if request.method == 'POST':
        X = int(request.POST.get('X'))
        Y = int(request.POST.get('Y'))
        if(request.POST.get('operator') == 'add'):
            result = X + Y
        elif(request.POST.get('operator') == 'subtrack'):
            result = X - Y
        elif(request.POST.get('operator') == 'multiply'):
            result = X * Y
        elif(request.POST.get('operator') == 'divide'):
            result = X / Y
    return render(request, 'homePOST.html', {'result': result})
