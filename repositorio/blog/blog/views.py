from django.shortcuts import render

# Create your views here.
def Home(request):  #UNA request es una petición
    return render(request, 'home.html')

def Nosotros(request):
    return render(request, 'nosotros.html')