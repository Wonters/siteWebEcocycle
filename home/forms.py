from django import forms
from django.forms import ModelForm


from .models import Contact
# form to get manual set values
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'#['name', 'email','phone_number','message']