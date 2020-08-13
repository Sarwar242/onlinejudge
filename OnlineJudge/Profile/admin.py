from django.contrib import admin
from Profile.forms import ProfileForm
from Profile.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display =[
            'user', 
            'google_id',
            'mobile_no',
            'cur_rating',
            'have_profile_image',
            'institution_id',
        ]
    form = ProfileForm

admin.site.register(Profile, ProfileAdmin)