from django.db import models
COMMUNITY_CHOICES = [("General","General"),("Baseball","Baseball"),("Basketball","Basketball"),("Tennis","Tennis")]
class Users(models.Model):
    UserName = models.CharField(max_length=12)
    Password = models.CharField(max_length=12)
    UserID = models.IntegerField()
    ImgUrl = models.CharField(max_length=50)
    def __str__(self):
        return self.UserID

class Posts(models.Model):
    Title = models.CharField(max_length=50)
    Post = models.TextField()
    UserID = models.IntegerField()
    PostID = models.IntegerField()
    CommunityID = models.IntegerField()
    ImgUrl = models.CharField(max_length=50)
    def __str__(self):
        return self.PostID

class Comments(models.Model):
    Comment = models.TextField()
    UserID = models.IntegerField()
    PostID = models.IntegerField()
    CommentID = models.IntegerField()
    def __str__(self):
        return self.CommentID

class Communities(models.Model):
    CommunityID = models.CharField(max_length=30)
    CommunityID = models.IntegerField()
    def __str__(self):
        return self.CommunityID