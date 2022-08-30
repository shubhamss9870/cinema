from django.db import models

# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class video(models.Model):


    s_no = models.IntegerField()
    video_title = models.CharField(max_length=1000,default="")
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_title
