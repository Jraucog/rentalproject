from django.shortcuts import render

# Create your views here.
def lista_view(request):
    return render(request, 'repuestos/lista.html')