from django.db import models
from celery import shared_task
import asyncio
from core.chatBot import ChatBot


@shared_task         #celery task for summerize and save to db
def generate_summary(article_id):      
    article_data=ArticleModel.objects.filter(id=article_id).first()
    chatbot = ChatBot()
    loop = asyncio.new_event_loop()  # Create a new async loop
    asyncio.set_event_loop(loop)  
    chatbot_summary = loop.run_until_complete(chatbot.summerize(article_data.description))  
    article_data.summary=chatbot_summary
    article_data.save()



class ArticleModel(models.Model):
    title = models.CharField(max_length=255,unique=True)
    status = models.IntegerField(default=0)  # publish=0 draft=1 for access level
    summary = models.CharField(max_length=500, blank=True, null=True)  
    description = models.TextField(blank=True,null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "article"

    def save(self, *args, **kwargs):
        is_new = self.pk is None  
        previous_description = None

        if not is_new:
            article = ArticleModel.objects.filter(pk=self.pk).only("description").first()
            if article:
                previous_description = article.description

        super().save(*args, **kwargs)  
        if is_new or (previous_description != self.description):
            generate_summary.delay(self.id)
            

class KnowledgeModel(models.Model):
    title = models.CharField(max_length=255,unique=True)
    status = models.IntegerField(default=0)  # publish=0 draft=1 for access level
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    articles = models.ManyToManyField("ArticleModel", blank=True)  


    def __str__(self):
        return self.title

    class Meta:
        db_table = "knowledge"
