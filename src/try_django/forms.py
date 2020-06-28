from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    emial = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea) 