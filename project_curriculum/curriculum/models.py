from django.db import models
# Create your models here.


class Curriculum(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    curriculum = models.FileField(upload_to='Curriculum_users',blank=True)
    linkedIn = models.URLField(blank=True)
    email = models.CharField(max_length=30,blank=True)
    title_the_presentation_letter = models.CharField(max_length=30,blank=True)
    presentation_letter = models.TextField(blank=True)

    def __str__(self):
        return "Curriculum: " + self.first_name







