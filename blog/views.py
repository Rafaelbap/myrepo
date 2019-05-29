from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):# cria função post_list que recebe um request
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #executa render que rendeiza/monta o modelo de acordo com o template blog/po_list.html. Retorna (return) o resultado.
                                                                    #A parte antes dos dois pontos ('post':post) é uma string, por isso está entre "".
