from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from pages.forms import SearchForm
from pages.models import Note
from django.contrib.postgres.search import SearchVector

class HomeView(TemplateView):
    template_name = 'home.html'

class NoteListView(ListView):
    model = Note
    template_name = 'list.html'
    paginate_by = 3

class NoteDetailView(DetailView):
    model = Note
    template_name = 'detail.html'
    slug_field = 'slug'

def sea(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Note.objects.annotate(
                search=SearchVector('name', 'text'),
                ).filter(search=query)
    return render(request, 'search.html',{'form': form,
                                          'query': query,
                                          'results': results})