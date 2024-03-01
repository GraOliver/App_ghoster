from django import forms

class UserCreation(forms.Form):
    username =forms.CharField(max_length=63,label='N')