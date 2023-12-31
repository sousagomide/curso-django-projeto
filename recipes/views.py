from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('title')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def category(request, category_id):
    '''
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('title')
    
    #category_name = getattr(getattr(recipes.first(), 'category', None), 'name', 'Not found');
    if not recipes:
        #return HttpResponse(content='Not found', status=404)
        raise Http404('Not found')
    '''
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('title'))
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}  - Category | '
    })

def recipe(request, id):
    recipe = Recipe.objects.filter(id=id, is_published=True).order_by('id').first()
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })

def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(Q(title__icontains=search_term) | Q(description__icontains=search_term)),
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'Search for "{ search_term }" | ',
        'search_term': search_term,
        'recipes': recipes
    })


