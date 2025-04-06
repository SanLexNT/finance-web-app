from enum import Enum
from django.db import models
from django.contrib.auth.models import User

# Enums

class Color(Enum):
    RED = 0
    BLUE = 1
    YELLOW = 2
    GREEN = 3
    PURPLE = 4
    BLACK = 5
    ORANGE = 6
    PINK = 7
    LIGHT_BLUE = 8
    GRAY = 9

class CategoryType(Enum):
    INCOME = 0
    OUTCOME = 1

# Enum variables

_COLORS = (
    (Color.RED, '#ff0000'),
    (Color.BLUE, '#0000ff'),
    (Color.YELLOW, '#ffff00'),
    (Color.GREEN, '#009933'),
    (Color.PURPLE, '#660066'),
    (Color.BLACK, '#000000'),
    (Color.ORANGE, '#ff9900'),
    (Color.PINK, '#ff6699'),
    (Color.LIGHT_BLUE, '#66ccff'),
    (Color.GRAY, '#595959'),
)

_CATEGORY_TYPES = (
    (CategoryType.INCOME, 'Доход'),
    (CategoryType.OUTCOME, 'Расход'),
)

# Models

class Category(models.Model):
    name = models.CharField(max_length=64)
    color = models.SmallIntegerField(choices=_COLORS)
    category_type = models.SmallIntegerField(choices=_CATEGORY_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} -- {self.name}'


class Account(models.Model):
    name = models.CharField(max_length=128)
    balance = models.DecimalField(max_digits=11, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Record(models.Model):
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.description[:50]}'



