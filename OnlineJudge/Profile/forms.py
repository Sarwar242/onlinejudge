from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user', 
            'google_id',
            'mobile_no',
            'cur_rating',
            'have_profile_image',
            'institution_id',
        ]
    def clean(self, *args, **kwargs):
        
        return super().clean(*args, **kwargs)