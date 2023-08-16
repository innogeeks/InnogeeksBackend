from django import forms
from .models import FormSubmission

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ('name', 'email', 'shortDesc', 'message', 'start_date', 'end_date', 'url')
        labels = {
            'start_date' : 'Registration Start Date',
            'end_date' : 'Registration End Date',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Event Name"}),
            'email': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Enter your Email"}),
            'shortDesc': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Small Description about event"}),
            'message': forms.Textarea(attrs={"rows": 5, 'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', 'placeholder': "Brief Details about event"}),
            'start_date': forms.DateInput(format=('%d/%m/%Y'),
                                          attrs={'class': 'form-control',
                                                 'placeholder': 'Select a date',
                                                 'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                                                 }),
            'end_date': forms.DateInput(format=('%d/%m/%Y'),
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Select a date',
                                               'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                                               }),
            'url': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Event Site URL"}),
        }
