from rest_framework import routers
from .views import KnowledgeViewSet,ArticleViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'knowledge', KnowledgeViewSet)
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    # path("add/", TestView.as_view(), name="add_numbers"),


]