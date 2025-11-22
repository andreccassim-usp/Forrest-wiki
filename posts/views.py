from django.shortcuts import render, get_object_or_404
from .models import Posts, Comentarios
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def list_posts(request):
    posts_list = Posts.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)
# Create your views here.


def detail_posts(request, posts_id):
    posts = get_object_or_404(Posts, pk=posts_id)
    context = {'posts': posts}
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
    
def update_posts(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        post.name = request.POST['name']
        post.categoria = request.POST['categoria']
        post.conteudo = request.POST['conteudo']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'posts/update.html', context)


def delete_posts(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)

def list_categorias(request):
    categorias = Posts.objects.values_list('categoria', flat=True).distinct()
    context = {'categorias': categorias}
    return render(request, 'posts/categorias.html', context)

def posts_by_category(request, categoria):
    posts = Posts.objects.filter(categoria=categoria)
    context = {'categoria': categoria, 'posts': posts}
    return render(request, 'posts/posts_by_category.html', context)