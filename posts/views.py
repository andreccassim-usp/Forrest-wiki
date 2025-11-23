from django.shortcuts import render, get_object_or_404
from .models import Posts, Comentarios, Categoria
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def add_comment(request, posts_id):
    post = get_object_or_404(Posts, id=posts_id)

    if request.method == "POST":
        text = request.POST.get("text")

        Comentarios.objects.create(
            author=request.user,
            text=text,
            post=post
        )

        return HttpResponseRedirect(
    reverse('posts:detail', args=(post.id,))
)

    return render(request, "posts/comment_create.html", {
        "post": post
    })

def list_posts(request):
    posts_list = Posts.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)


def detail_posts(request, posts_id):
    posts = get_object_or_404(Posts, pk=posts_id)
    comentarios = Comentarios.objects.filter(post=posts).order_by('id')
    context = {
        'posts': posts,
        'comentarios': comentarios,
    }
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
        nome = request.POST['name']
        conteudo = request.POST['conteudo']
        categorias_ids = request.POST.getlist("categorias")

        post = Posts.objects.create(
            name=nome,
            conteudo=conteudo,
        )

        if categorias_ids:
            post.categorias.set(categorias_ids)

        return HttpResponseRedirect(reverse('posts:index'))

    # GET -> enviar lista de categorias para o <select>
    categorias = Categoria.objects.all()
    return render(request, 'posts/create.html', {'categorias': categorias})


def update_posts(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        post.name = request.POST['name']
        post.conteudo = request.POST['conteudo']

        categorias_ids = request.POST.getlist("categorias")
        post.save()

        if categorias_ids:
            post.categorias.set(categorias_ids)
        else:
            post.categorias.clear()

        return HttpResponseRedirect(reverse('posts:detail', args=(post.id,)))

    categorias = Categoria.objects.all()
    context = {'post': post, 'categorias': categorias}
    return render(request, 'posts/update.html', context)


def delete_posts(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)

def list_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'posts/categorias.html', {'categorias': categorias})

def posts_by_category(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    posts = categoria.posts.all()  # graças ao related_name="posts"
    context = {'categoria': categoria, 'posts': posts}
    return render(request, 'posts/posts_by_category.html', context)