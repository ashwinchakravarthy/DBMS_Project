from django import forms
from .models import Volunteers, Branch


class volunteersForm(forms.ModelForm):
    class Meta:
        model = Volunteers
        # fieldone = forms.ModelChoiceField(
        #     queryset=Branch.objects.all(), empty_label=None)

        fields = '__all__'

    # class RawVolForm(forms.Form):
    #     vol_name = forms.CharField(
    #         widget=forms.TextInput({"placeholder": 'NAME'}))
    #     vol_id = forms.IntegerField(
    #         widget=forms.TextInput({"placeholder": 'ID'}))
