from django.shortcuts import render

# Create your views here.
def home(request):
    result = 0
    if request.method == 'POST':
        X = int(request.POST.get('X'))
        Y = int(request.POST.get('Y'))
        result = X + Y
    return render(request, 'home.html', {'result': result})
