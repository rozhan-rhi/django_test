from rest_framework import serializers
from .models import ArticleModel,KnowledgeModel

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleModel
        fields='__all__'
        extra_kwargs = {
            "created_at": {"read_only": True},
            "summary":{"read_only": True}
        }


class KnowledgeSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(queryset=ArticleModel.objects.all(), many=True, required=False)
    article_details = ArticleSerializer(source="articles", many=True, read_only=True)
    class Meta:
        model=KnowledgeModel
        fields='__all__'
        extra_kwargs = {
            "created_at": {"read_only": True}
        }
