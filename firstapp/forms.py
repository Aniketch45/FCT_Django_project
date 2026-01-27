from django import forms

class StudentForm(forms.Form):
    sname = forms.CharField()
    semail = forms.EmailField()

class StudentForm2(forms.Form):
    sno = forms.IntegerField()
    name = forms.CharField()
    sfees = forms.DecimalField()
    