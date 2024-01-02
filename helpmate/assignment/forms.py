from assignment.models import Assignment
from django import forms

class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields="__all__"