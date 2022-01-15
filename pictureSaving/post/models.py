from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
# 4 table  post
class Post(models.Model):
    postId =models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    caption = models.CharField(max_length=500, blank=True)
    numberHeart=models.IntegerField(default=0)
    numberComment=models.IntegerField(default=0)
    description = models.TextField(max_length=500, blank=True)
    dateCreated = models.DateTimeField('date created',auto_now_add=True)
    dateModified = models.DateTimeField('date modified',auto_now=True)
    def __str__(self):
        return self.caption
# 1 table profile have one to one relationship with user to extend the user table.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500,null=True, blank=True)
    crushId = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# 2 table album
class Album(models.Model):
    albumId= models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    topic = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=500, blank=True)
    SHARE_CHOICES = (
        ('A', 'Public',),
        ('D', 'Private',),
    )
    shareMode = models.CharField(
        max_length=1,
        choices=SHARE_CHOICES,
        default='D'
    )
    dateCreated = models.DateTimeField('date created',auto_now_add=True)
    dateModified = models.DateTimeField('date modified',auto_now=True)
    def __str__(self):
        return self.topic
# 3 table album post
class AlbumPost(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    postId= models.ForeignKey(Post, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField('date created',auto_now_add=True)
   

# 5 Image
class Image(models.Model):
    imageId =models.AutoField(primary_key=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=500, blank=True)
    path = models.ImageField()
    dateCreated = models.DateTimeField('date created',auto_now_add=True)
    dateModified = models.DateTimeField('date modified',auto_now=True)
    def __str__(self):
        return self.name
# 6 userHear the junction of user makes heart to post
class UserHeart(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField('date created',auto_now_add=True)
# 7 UserComment the junction of user makes comment to post
class UserComment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, blank=True)
    dateCreated = models.DateTimeField('date created',auto_now_add=True)
    dateModified = models.DateTimeField('date modified',auto_now=True)
    def __str__(self):
        return self.content
#9 Icon
class Icon(models.Model):
    albumId = models.ForeignKey(Album,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    userId = models.ForeignKey( User,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    path = models.ImageField()
    dateCreated = models.DateTimeField('date created',auto_now_add=True)
    dateModified = models.DateTimeField('date modified',auto_now=True)
