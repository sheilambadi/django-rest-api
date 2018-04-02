from django.db import models

class employees(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname

     #remove additional s in admin panel
    class Meta:
        verbose_name_plural = 'Employees'