from django.shortcuts import render

# Create your views here.
def lista_post(request):
    return render(request, 'cinema_html/filme_post', {})
