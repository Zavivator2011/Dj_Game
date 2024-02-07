from django.shortcuts import render

from games.models import Category, Game, GameScreenshots

def home_page(request, category=None):
    categories = Category.objects.all()
    games = Game.objects.all()
    
    if category:
        games = Game.objects.filter(category__slug=category)
    
    if request.GET:
        games = Game.objects.filter(name__icontains=request.GET['q'])
    
    content = {
        "categories":categories,
        "games": games,
    }
    return render(request,'home.html', context=content)


def detail_page(request, game_id):
    categories = Category.objects.all()
    game = Game.objects.get(id=game_id)
    game_screenshots = GameScreenshots.objects.filter(game=game)
    context = {
        "categories":categories,
        "game": game,
        "game_screenshots": game_screenshots
    }
    return render(request, 'detail_page.html', context=context)