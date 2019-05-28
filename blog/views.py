from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):# cria função post_list que recebe um request
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #executa render que rendeiza/monta o modelo de acordo com o template blog/po_list.html. Retorna (return) o resultado.
