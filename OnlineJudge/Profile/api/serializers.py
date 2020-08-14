from rest_framework import serializers
from Profile.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
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

        