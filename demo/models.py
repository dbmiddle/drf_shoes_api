from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'RE'
    ORANGE = 'OR'
    YELLOW = 'YE'
    GREEN = 'GR'
    BLUE = 'BLU'
    INDIGO = 'IN'
    VIOLET = 'VI'
    WHITE = 'WH'
    BLACK = 'BLK'
    SHOE_COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]
    color_name = models.CharField(
        max_length=3, choices=SHOE_COLOR_CHOICES, default=WHITE)

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)

# Joe didn't actually grow up on the African Savanna, but he did last 3 episodes there on Survivor!!
