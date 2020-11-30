from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


# class DateInput(forms.DateInput):
#     input_type = forms.DateField(widget=DateInput)

class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stud_name', 'stud_email', 'stud_USN', 'stud_college']


class EventForm(forms.ModelForm):
    # event_date_time_field = forms.DateField(widget=DateInput)

    class Meta:
        widgets = {'event_date_time': DateInput}
        model = Event

        fields = ['event_name', 'event_date_time',  'event_description', 'event_price',
                  'event_fee', 'event_maxteams', 'event_location']


class JuryForm(forms.ModelForm):
    class Meta:
        model = Jury
        fields = '__all__'
