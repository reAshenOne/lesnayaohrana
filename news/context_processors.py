from .models import NewsPage

def latest_news(request):
    latest_news = NewsPage.objects.live().order_by('-first_published_at')[:3]  # Получаем три последние новости
    return {'latest_news': latest_news}