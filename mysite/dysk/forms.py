from django import forms
from .models import Document
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        # fields = '__all__'
        fields = [
            'id_katalogu','myfile'
        ]