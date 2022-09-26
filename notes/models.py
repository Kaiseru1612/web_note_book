from django.db import models

# Create your models here.

class Note(models.Model):
    """
    class Note
        titile str
        content str
        date_crated datetime
    """
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

