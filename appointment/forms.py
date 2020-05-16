from django import forms

class SimpleForm(forms.Form):
    p_name = forms.CharField(max_length=30)
    sex = forms.CharField(max_length=6)
    age = forms.IntegerField()
    disease_type = forms.CharField()
    email = forms.CharField(max_length=20)
    phone = forms.IntegerField()
