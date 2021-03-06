import datetime
from django.db import models


class Diner(models.Model):
    name = models.CharField(max_length=32)
    opens = models.TimeField(default=datetime.time(11, 00))
    closes = models.TimeField(default=datetime.time(22, 00))


class Area(models.Model):
    name = models.CharField(max_length=32)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    diners = models.ManyToManyField(
        Diner, 
        through="DeliveryArea",
        related_name="deliver_area"
    )


class DeliveryArea(models.Model):
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name="delivery_area")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="area_fee")
    fee = models.IntegerField(default=1000)


class Menu(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    diner = models.ForeignKey(
        Diner, 
        on_delete=models.CASCADE, 
        related_name="diner_menus"
    )


class MenuOptionGroup(models.Model):
    name = models.CharField(max_length=32)
    mandatory = models.BooleanField(default=False)
    select_min = models.IntegerField(default=0)
    select_max = models.IntegerField(default=1)
    for_menu = models.ForeignKey(
        Menu, 
        on_delete=models.CASCADE, 
        related_name="menu_option_group"
    )



class FoodCategory(models.Model):
    name = models.CharField(max_length=32)
    category_diners = models.ManyToManyField(
        Diner,
        related_name="diner_categories"
    )
