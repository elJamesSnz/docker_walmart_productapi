from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import json

from .models import Categoria
from .scraper import scrape_walmart


class ScrapeView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        url = body.get('url')
        categories = scrape_walmart(url)
        return JsonResponse(categories, safe=False)
    
    def get(self, request):        
        return Response(200)