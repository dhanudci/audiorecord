from django import forms
from .models import AudioRecord

class AudioRecordForm(forms.ModelForm):
    class Meta:
        model = AudioRecord
        fields = ['phonenumber']

