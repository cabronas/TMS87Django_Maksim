from django.db import models


# Create your models here.
class AImage(models.Model):
    url = models.URLField()
    kind = models.CharField(default='cat',
                            max_length=5,
                            choices=[('cat', 'Cat'), ('dog', 'Dog')])
    date_of_creation = models.DateField(auto_now_add=True)
    type = models.CharField(default='png',max_length=5, choices=[('png', 'PNG'), ('gif', 'GIF'), ('jpg', 'JGP'), ('jpeg', 'JPEG')])
