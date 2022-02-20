from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='blog_images/')

    def get_summary(self):
        return self.text