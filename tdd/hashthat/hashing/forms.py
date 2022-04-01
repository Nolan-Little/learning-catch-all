from django import forms
from .models import Hash
import hashlib

class HashForm(forms.ModelForm):
    class Meta:
        model = Hash
        fields = ["text"]

    text = forms.CharField(label="Enter hash here:", widget=forms.Textarea)

    def save(self, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        instance.hash = hashlib.sha256(instance.text.encode('utf-8')).hexdigest()
        instance.save()

        return instance
