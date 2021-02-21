from django.db import models


class Transaction(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField()
    type = models.CharField(max_length=100)
    date_added = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.amount} {self.type} {self.date_added}'
