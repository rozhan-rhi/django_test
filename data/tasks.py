# from celery import shared_task
# import asyncio
# from core.chatBot import ChatBot
# from data.models import ArticleModel


# @shared_task
# def generate_summary(article_id):       #celery task
#     article_data=ArticleModel.objects.filter(id=article_id).first()
#     print(article_data)
#     chatbot = ChatBot()
#     loop = asyncio.new_event_loop()  # Create a new async loop
#     asyncio.set_event_loop(loop)  
#     chatbot_summary = loop.run_until_complete(chatbot.summerize(article_data.description))  
#     print(chatbot_summary)
#     article_data.summary=chatbot_summary
#     article_data.save()