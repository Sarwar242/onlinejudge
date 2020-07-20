from django.contrib import admin
from Problem.models import Problem_Tags, Problems,Inputs
# Register your models here.
admin.site.register(Problems)
admin.site.register(Problem_Tags)
admin.site.register(Inputs)