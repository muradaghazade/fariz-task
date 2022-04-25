from django.views.generic import ListView, DetailView
from .models import Article

class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by("-id")

    def get_queryset(self):
        queryset = Article.objects.order_by("-id")
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class ArticleDetail(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'article'
