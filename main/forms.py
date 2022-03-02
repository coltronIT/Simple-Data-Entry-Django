from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    age = forms.IntegerField(label="Age", max_value=150, required=False)
    title = forms.CharField(label="Title", max_length=50)
    hometown = forms.CharField(label="hometown", max_length=50, required=False)