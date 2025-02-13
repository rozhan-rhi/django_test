from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ArticleModel,KnowledgeModel
from .serializers import ArticleSerializer,KnowledgeSerializer
from core.chatBot import ChatBot
import asyncio

class KnowledgeViewSet(viewsets.ModelViewSet):
    queryset=KnowledgeModel.objects.all()
    serializer_class=KnowledgeSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return KnowledgeModel.objects.all()  # Superusers see everything
        return KnowledgeModel.objects.filter(status=0, articles__status=0).distinct()  



class ArticleViewSet(viewsets.ModelViewSet):
    queryset=ArticleModel.objects.all()
    serializer_class=ArticleSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ArticleModel.objects.all()  # Superusers see everything
        return ArticleModel.objects.filter(status=0)

    
