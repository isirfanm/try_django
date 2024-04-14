from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Article
from .forms import ArticleModelForm


# Create your views here.
class ArticleCreateView(CreateView):
    template_name = "blog/article_create.html"
    form_class = ArticleModelForm
    # success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self) -> str:
    #     return "/"

class ArticleListView(ListView):
    # template_name = "blog/article_list.html"
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    # queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)


class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ArticleDeleteView(DeleteView):

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
    
    def get_success_url(self) -> str:
        return reverse("article-list")