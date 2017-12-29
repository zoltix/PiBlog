# -*-coding:Utf-8 -*
""" définition des vues """
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,reverse
from .models import Article, Comment
from .forms import CommentForm



def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

    return render(request, 'blog/accueil.html', {'articles': articles})


def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre
    """
    article = get_object_or_404(Article, slug=slug)
    commentaires = Comment.objects.filter(article__id=article.id, is_visible=True).order_by('-date')#[:4]
    form = CommentForm(request.POST or None)
    if form.is_valid():
        contenu= form.cleaned_data['contenu']
        pseudo = form.cleaned_data['pseudo']
        email = form.cleaned_data['email']
        contenu = form.cleaned_data['contenu']
        com =Comment(pseudo=pseudo, email=email, contenu=contenu)
        com.article = article
        com.save()
        form  = CommentForm()
        #return HttpResponseRedirect(reverse("blog.views.lire_article"))
    return render(request, 'blog/lire_article.html', locals())
