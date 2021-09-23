from django.db import models
COMMUNITY_CHOICES = [("General","General"),("Baseball","Baseball"),("Basketball","Basketball"),("Tennis","Tennis")]
class Users(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    def __str__(self):
        return self.username

class Posts(models.Model):
    #username = models.CharField(max_length=12)
    #community_id = models.CharField(max_length=12)
    #post_id = models.IntegerField()
    title = models.CharField(max_length=255)
    post = models.TextField()
    def __str__(self):
        return self.post_id
