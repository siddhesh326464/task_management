from django.db import models


# Create your models here.
class Project:
    class Meta:
        db_table = "project"
        verbose_name = "Projects"
        verbose_name_plural = "Project"
    name = models.CharField(max_length=50,unique=True,null=True,blank=True)
    user = models.ForeignKey('Account',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post:
    class Meta:
        db_table = "post"
        verbose_name = "Posts"
        verbose_name_plural = "Post"
    title = models.CharField(max_length=50,null=True,blank=True)
    detail = models.TextField(null=True,blank=True)
    user = models.ForeignKey('Account',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('Account',on_delete=models.CASCADE)
    updated_by = models.ForeignKey('Account',on_delete=models.CASCADE)

class UserPostAssociation:
    class Meta:
        db_table = "userpostassociation"
        verbose_name = "UserPostAssociations"
        verbose_name_plural = "UserPostAssociation"

    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    user = models.ForeignKey('Account',on_delete=models.CASCADE)

        
