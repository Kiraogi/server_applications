from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
