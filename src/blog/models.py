from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    images = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
