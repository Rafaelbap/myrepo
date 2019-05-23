from django.shortcuts import render

# Create your views here.

def post_list(request):# cria função post_list que recebe um request
    return render(request, 'blog/post_list.html', {}) #executa render que rendeiza/monta o modelo de acor com o template blog/po_list.html. Retorna (return) o resultado.
