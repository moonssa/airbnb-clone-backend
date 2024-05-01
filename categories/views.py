# from django.shortcuts import render
# from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view()
def categories(request):
    all_categoriees = Category.objects.all()
    serializer = CategorySerializer(all_categoriees, many=True)
    return Response(
        {
            "ok": True,
            "categories": serializer.data,
        },
    )
