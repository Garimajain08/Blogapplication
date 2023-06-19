from django.db import models
from froala_editor.fields import FroalaField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now
from .utlis import *


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

class Blogmodel(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField()
    slug = models.SlugField( max_length=100,blank=True,null=True)
    images = models.ImageField ( default = " " ,upload_to = "images/")
    created_at = models.DateTimeField (auto_now_add=True )
    user = models.ForeignKey(User,blank=True , null = True , on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default = 0)
    likes = models.ManyToManyField(User,related_name='blog_post')

    def __str__(self):
        return (self.title)

@receiver(pre_save, sender=Blogmodel)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)

class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,blank=True , null = True , on_delete = models.CASCADE)
    post = models.ForeignKey(Blogmodel,on_delete = models.CASCADE)
    parent = models.ForeignKey('self',null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return (self.comment)




