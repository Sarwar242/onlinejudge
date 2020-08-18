from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Profile
        fields = [
            'user', 
            'google_id',
            'mobile_no',
            'cur_rating',
            'have_profile_image',
            'institution_id',
        ]
        read_only_fields  = [
            'user',
            'cur_rating',
        ]
    

