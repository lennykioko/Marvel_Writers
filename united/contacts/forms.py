"""Creates the form fields to be used by crispy forms"""
from django import forms


class ContactForm(forms.Form):
    """Creates form fields to be used by crispy forms"""    
    name = forms.CharField(required=False, max_length=50)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
    