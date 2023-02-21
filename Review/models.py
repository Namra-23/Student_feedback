from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    gmail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    student_id=models.CharField(max_length=10,default="20CEUOS000")
    
    def GetUserByEmail(gmail):
        try:
            return User.objects.get(gmail=gmail)
        except:
            return False