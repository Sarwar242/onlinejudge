from django.contrib import admin
from Problem.models import Problem_Tag, Problem, Input
# Register your models here.
admin.site.register(Problem)
admin.site.register(Problem_Tag)
admin.site.register(Input)