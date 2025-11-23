from django.shortcuts import render, get_object_or_404
from .models import Posts, Comentarios
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def list_posts(request):
    posts_list = Posts.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)
# Create your views here.

def post(request, post_id):
    post = post_data[post_id - 1]
    return HttpResponse(
        f'Detalhes do filme {post["name"]} ({movie["release_year"]})')

def detail_posts(request, post_id):
    post = get_object_or_404(pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Posts.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

def create_posts(request):
    if request.method == 'POST':
        post_name = request.POST['name']
        post_categoria = request.POST['categoria']
        post_conteudo = request.POST['conteudo']
        post = Posts(name=post_name,
                      categoria=post_categoria,
                      conteudo= post_conteudo)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:index'))
    else:
        return render(request, 'posts/create.html', {})