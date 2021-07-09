from django.db import models

class Project(models.Model):
    tilte=models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="protfolio/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.tilte
