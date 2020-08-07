from django.contrib import admin
from Rating.models import Rating_Status,Rating_Change
# Register your models here.
admin.site.register(Rating_Status)
admin.site.register(Rating_Change)