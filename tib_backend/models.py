from django.db import models


class Person(models.Model):
    name = models.TextField()
    years_range_begin = models.IntegerField()
    years_range_end = models.IntegerField()


class Sentence(models.Model):
    sentence = models.TextField()