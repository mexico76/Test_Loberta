from django.db import models

class TestLink(models.Model):
    link = models.URLField(verbose_name='Reference')
