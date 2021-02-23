from django import forms
class NameForm(forms.Form):
    first_name=forms.CharField(label="enter first name",max_length=10)
    last_name=forms.CharField(label="Enter first name",max_length=10)