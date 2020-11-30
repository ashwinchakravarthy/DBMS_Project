from django.db import models
from datetime import datetime

# Create your models here.


class Branch(models.Model):

    br_id = models.IntegerField()
    br_name = models.CharField(max_length=20)

    def __str__(self):
        return self.br_name
    # volunteers = models.ManyToManyField(Volunteers)


class Volunteers(models.Model):
    vol_name = models.CharField(max_length=20)
    vol_id = models.IntegerField()

    branch = models.ManyToManyField(Branch, blank=True)


# class Volunteer(models.Model):
#     vol_ID = models.IntegerField()
#     vol_name = models.CharField(max_length=30)
#     vol_phno = models.IntegerField()
#     vol_email = models.EmailField()
#     vol_address = models.TextField(max_length=100)
#     vol_age = models.IntegerField()
#     vol_gender = models.CharField(max_length=10)
#     vol_DOJ = models.DateField(_("Date"), default=vol_DOJ.today)
#     vol_occupation = models.CharField(max_length=30)


# class ClinicAddress(models.Model):
#     cl_ID = models.IntegerField()
#     cl_address = models.CharField(max_length=50)
#     cl_phno = models.IntegerField()
#     cl_timings = models.CharField(max_length=10)


# class Medicine(models.Model):
#     med_id = models.IntegerField()
#     med_name = models.CharField(max_length=50)
#     med_avail = models.BooleanField()


# class VolunteerMedicine(models.Model):
