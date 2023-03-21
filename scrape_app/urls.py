from django.urls import path
from scrape_app.views import ScrapeView


urlpatterns = [
    path('api/scraper/categoria/', ScrapeView.as_view(), )
]