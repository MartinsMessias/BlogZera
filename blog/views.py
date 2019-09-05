from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage
from . import models
from django.contrib import messages


@login_required
def accounts(request):
    return HttpResponse(404)


def posts_blog(requests):
    page = requests.GET.get('page', 1)
    paginator = Paginator(models.Postagem.objects.all().order_by('data_publicacao').reverse(), 3)

    try:
        dados = paginator.page(page)
    except InvalidPage:
        dados = paginator.page(1)

    return render(requests, 'blog/postagens.html', {'dados': dados})


def post_blog(requests, post_id):
    dados = models.Postagem.objects.get(id=post_id)
    return render(requests, 'blog/post.html', {'dados': dados})


def all_post_blog(requests):
    dados = models.Postagem.objects.all().order_by('data_publicacao').reverse()
    return render(requests, 'blog/allposts.html', {'dados': dados})


def contact_blog(request):
    return render(request, 'blog/contact.html')

def about_blog(request):
    return render(request, 'blog/about.html')
