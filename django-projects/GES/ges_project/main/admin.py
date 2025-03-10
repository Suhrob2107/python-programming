from django.contrib import admin
from django.contrib.admin import ModelAdmin

from main.models import *

######################################

class FilialAdmin(admin.ModelAdmin):
    pass

admin.site.register(Filial,FilialAdmin)

#####################################
class RegisterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Register,RegisterAdmin)

######################################
"""
class CourseAdmin(admin,ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)
"""

from django.contrib import admin
from .models import Course  # Make sure you import the model you're customizing

class CourseAdmin(admin.ModelAdmin):
    # Customizations for the Course model in the admin interface
    pass

# Register your model and its admin customization
admin.site.register(Course, CourseAdmin)


#######################################

class PrizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prize,PrizeAdmin)


#######################################

class InformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Information,InformationAdmin)



########################################

class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff,StaffAdmin)


#########################################

class VacancyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vacancy,VacancyAdmin)
# Register your models here.
