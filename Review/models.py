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
    
    def __str__(self):
        return self.name
    

class Semester(models.Model):
    name=models.CharField(max_length=5)

    def __int__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
class Subject(models.Model):
    semester=models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Faculty(models.Model):

    BATCH = (
        ('A','A'),
        ('B','B'),
    )

    name=models.CharField(max_length=100)
    gmail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    semester=models.ForeignKey(Semester, on_delete=models.SET_NULL, blank=True, null=True)
    subject=models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True)
    batch=models.CharField(verbose_name='batches',max_length=5,choices=BATCH)
    
    # def GetUserByEmail(gmail):
    #     try:
    #         return User.objects.get(gmail=gmail)
    #     except:
    #         return False

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name
    
    def GetUserByEmail(gmail):
        try:
            return Faculty.objects.get(gmail=gmail)
        except:
            return False