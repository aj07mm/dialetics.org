from enum import Enum
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=150)


class Argument(models.Model):
    source = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[
        ("PRO", 'pro'),
        ("CON", 'con'),
    ])
    topic = models.ForeignKey(
        'topics.Topic',
        on_delete=models.CASCADE,
        related_name="arguments"
    )
