from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer=models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, null=False)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=True,null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80] 