from django.db import models

# Create your models here.
class Commerce(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.name

# from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

