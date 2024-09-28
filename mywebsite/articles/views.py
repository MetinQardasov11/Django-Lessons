from django.shortcuts import render
from .models import Article

# Create your views here.

def article_view(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/article.html', context)


def science_view(request):    
    return render(request, 'articles/science.html')
