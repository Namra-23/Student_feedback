from django.db import models
from django.urls import reverse
from Home.models import Teacher
from Review.models import Faculty, Semester

class FeedbackData(models.Model):

    CHOICES = (
            (1,'Unsatisfactory'),
            (2,'Satisfactory'),
            (3,'Good'),
            (4,'Very Good'),
            (5,'Outstanding')
            )

    date_submitted = models.DateTimeField(auto_now=True)

    teacher_name = models.ForeignKey(Faculty, verbose_name='Name of Teacher',
                                     on_delete=models.CASCADE)

    semester = models.ForeignKey(Semester, verbose_name='Semester',
                                  on_delete=models.SET_NULL, blank=True, null=True)

    punctuality = models.PositiveSmallIntegerField(verbose_name='The teacher is punctual in coming to class',
                                   default = None, blank=False, null=False,
                                   choices=CHOICES)

    portion = models.PositiveSmallIntegerField(verbose_name='The teacher completes portions at the appropriate time',
                               default = None, blank=False, null=False,
                               choices=CHOICES)

    doubt = models.PositiveSmallIntegerField(verbose_name='The teacher takes in effort to clear your doubts',
                             default = None, blank=False, null=False,
                             choices=CHOICES)

    interactive = models.PositiveSmallIntegerField(verbose_name='The teacher makes the class interactive',
                                   default = None, blank=False, null=False,
                                   choices=CHOICES)
    total = models.PositiveIntegerField()
    average = models.FloatField()
    comments = models.TextField(verbose_name='Any other feedback (your comments)',
                                blank=True)

    def save(self, *args, **kwargs):
        self.total = (self.punctuality + self.portion + self.doubt + self.interactive)
        self.average = (self.punctuality + self.portion + self.doubt + self.interactive)/4
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Feedback Data'
        verbose_name_plural = 'Feedback Data'

    def __str__(self):
        return self.teacher_name.name

    def get_absolute_url(self):
        return reverse('SuccessView')

    def __init__(self, *args, **kwargs):
        super(FeedbackData, self).__init__(*args, **kwargs)
        if 'teacher_name' in kwargs:
            self.fields['semester'].queryset = Semester.objects.filter(
                faculty=kwargs['teacher_name']
            )
