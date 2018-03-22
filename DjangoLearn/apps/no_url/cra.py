from django import forms
class Addcra(forms.Form):
    userName = forms.CharField()
    passWord = forms.CharField()
    url_login = forms.CharField()
    url_next = forms.CharField()