from django.shortcuts import render
from django.utils import timezone
from .models import PostFilmes
# Create your views here.
def lista_post(request):
    posts = PostFilmes.objects.filter(data_publicacao__lte=timezone.now()).order_by('titulo')
    return render(request, 'cinema_html/filme_post', {'posts': posts})

