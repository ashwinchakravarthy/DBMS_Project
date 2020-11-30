from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class Role(models.Model):
#     role_name = models.CharField(max_length=20)

class Location(models.Model):
    loc_name = models.CharField(max_length=20)

    def __str__(self):
        return self.loc_name


class Event(models.Model):
    event_name = models.CharField(max_length=20)
    event_date_time = models.DateTimeField(blank=True)
    event_description = models.TextField(max_length=1000)
    event_price = models.IntegerField()
    event_fee = models.IntegerField()
    event_maxteams = models.IntegerField()
    event_location = models.ForeignKey(
        Location, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.event_name


class Student(models.Model):
    stud_name = models.CharField(max_length=20)
    stud_email = models.EmailField()
    stud_college = models.CharField(max_length=50)
    stud_USN = models.CharField(max_length=10)
    stud_part_events = models.ForeignKey(
        Event, default=5, on_delete=models.CASCADE)

    def __str__(self):
        return self.stud_name


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vol_USN = models.CharField(max_length=10)
    vol_event = models.ForeignKey(
        Event, default=5, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.user.username


class Result(models.Model):
    res_event = models.ForeignKey(
        Event, default=5, on_delete=models.SET_DEFAULT)
    winner = models.ForeignKey(
        Student, default=1, related_name='event_winner', on_delete=models.SET_DEFAULT)
    runner = models.ForeignKey(
        Student, default=1, related_name='event_runner', on_delete=models.SET_DEFAULT)


class Jury(models.Model):
    jury_name = models.CharField(max_length=20)
    jury_email = models.EmailField()
    event = models.ForeignKey(Event, default=5, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.jury_name

    # class Person(models.Model):
    #     per_name = models.CharField(max_length=20)

    # //to be created student,volunteers,jury,event,location,results
