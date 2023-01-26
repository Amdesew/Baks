from django.db import models

#h1, t1, auto, d1, moter

class HezbeOne(models.Model):
    name = models.CharField(max_length=200)
    result = models.CharField(max_length=300)

class TaxiOne(models.Model):
    name = models.CharField(max_length=200)
    result = models.CharField(max_length=300)

class Automobile(models.Model):
    name = models.CharField(max_length=200)
    result = models.CharField(max_length=300)

class DerekOne(models.Model):
    name = models.CharField(max_length=200)
    result = models.CharField(max_length=300)

class Moter(models.Model):
    name = models.CharField(max_length=200)
    result = models.CharField(max_length=300)
