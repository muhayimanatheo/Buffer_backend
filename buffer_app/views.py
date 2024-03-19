from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from.models import Publication
from.serializers import AdminPublicationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import JsonResponse
from rest_framework import status
# Create your views here.
def index(request):
    return HttpResponse("hello world")

@csrf_exempt
@api_view(['GET', 'POST'])
def AdminPublicationApi(request):
    if request.method == 'GET':
        selectedData = Publication.objects.all()
        serializer = AdminPublicationSerializer(selectedData, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminPublicationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
           return JsonResponse(serializer.errors, status=400)
