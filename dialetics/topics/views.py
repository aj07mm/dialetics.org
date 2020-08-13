from django.shortcuts import render
from django.views.generic import TemplateView
from topics import models

class TopicView(TemplateView):
    template_name = "topic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic_name"] = kwargs['topic_name']
        topic = models.Topic.objects.filter(name=kwargs['topic_name']).first()

        if topic:
            context["arguments"] = topic.arguments.all()

        return context
