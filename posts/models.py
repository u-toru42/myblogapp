from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    # 画像認識
    image = models.ImageField(upload_to='media/')
    # 長めのテキストを打てるように
    body = models.TextField()

    # 投稿の文字列:タイトルを返すように
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]