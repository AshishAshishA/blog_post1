from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories  = models.ManyToManyField("Category" ,related_name="posts")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.post} by {self.author}"