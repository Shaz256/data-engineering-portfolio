from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"   # ⭐ tells Django to use existing table
        managed = False         # ⭐ VERY IMPORTANT (do not let Django recreate)


