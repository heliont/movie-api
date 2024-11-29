from django.shortcuts import render


# Página de Erro 400
def handler404(request, exception):
    return render(request, '404.html')


# Página de erro 500
def handler500(request):
    return render(request, '500.html')
