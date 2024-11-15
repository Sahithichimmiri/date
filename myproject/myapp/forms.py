from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    # Custom input format for dates
    start_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )
    end_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )

    class Meta:
        model = Employee
        fields = ['start_date', 'end_date']  # Fields to include in the form