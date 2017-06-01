from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import PostFilmes, Comentario
# Create your views here.
def lista_post(request):
    posts = PostFilmes.objects.filter(data_publicacao__lte=timezone.now()).order_by('titulo')
    return render(request, 'cinema_html/filme_post', {'posts': posts})
def detalhes_post(request, pk):
    post = get_object_or_404(PostFilmes, pk=pk)
    l = Comentario.objects.filter()
    return render(request, 'cinema_html/detalhes_post', {'post':post, 'l': l})
