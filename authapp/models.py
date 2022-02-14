from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
# Create your models here.



class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete = models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete = models.CASCADE)
class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True,related_name="friends")
    
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    

    
