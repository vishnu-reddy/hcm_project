from django import forms
from cornerstone.models import CornerstoneUserProfile

from mptt.forms import TreeNodeChoiceField

class CornerstoneUserProfileForm(forms.ModelForm):
    class Meta:
        model = CornerstoneUserProfile
        fields = ['first_name', 'last_name']
