from django.db import models


class Diner(models.Model):
    name = models.CharField(max_length=32)


class Menu(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    diner = models.ForeignKey(
        Diner, 
        on_delete=models.CASCADE, 
        related_name="diner_menus"
    )
