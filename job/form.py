
from django.db.models import fields
from . models import Apply, Job, Contact
from django import forms

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'cv', 'letter']
        labels = {
            "name": "Nom et prenom",
            "letter": "lettre"
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', 'owner',)
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
