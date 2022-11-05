from django.forms import ModelForm
from .models import DemendeUnAppel

class DemendeUnAppelForm(ModelForm):
    class Meta:
        model = DemendeUnAppel
        fields = '__all__'