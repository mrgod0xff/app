from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError

# Create your views here.
from .models import Article, Categorie, Nouveaute
from titrologie.models import Revue

def actualites(request):
    articles = Article.objects.all()
    cartego  = Categorie.objects.all()
    revue = Revue.objects.all()[:5]

    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        'title': 'Actualité Ivoirienne',
        'articles': articles,
        'category': cartego,
        'revue': revue,
        'paginate': True
    }

    return render(request, 'actualite/listing.html', context)


@transaction.atomic
def see_more(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article_id': article.id,
        'article_titre': article.titre,
        'content': article.content,
        'type': article.genre,
        'thumbnail': article.image
    }
    return render(request, 'actualite/see-more.html', context)