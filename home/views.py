from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import renderers

class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {'count': len(data), 'results': data}
        return super().render(response_data, accepted_media_type, renderer_context)

# Create your views here.

# default home view
def homepage(request, *args, **kwargs):
    return render(request, 'home.html')

class MovieList(APIView):
    renderer_classes = [CustomRenderer]
    def get(self, request):
        queryset = Film.objects.all()[:10]
        output = []
        for data in queryset:
            serialized_data = FilmSerializers(data)
            output.append(serialized_data.data)
        return Response(output)

class MovieSearch(APIView):
    renderer_classes = [CustomRenderer]  
    def post(self, request):
        if not request.data:
            return Response({"success":False})
        movie_name = request.data.get('movie',"")
        queryset1 = Rental.objects.all()
        queryset = Film.objects.filter(title__icontains=movie_name)
        output = []
        if len(queryset) >= 1:
            for data in queryset:
                serialized_data = FilmSerializers(data)
                output.append(serialized_data.data)
        return Response(output)
