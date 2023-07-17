from django.contrib import admin
from .models import Skill, Education, Experience, Personal, Social, Testimonials, Blog, PersonalInfo


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    list_filter = ['value']
    search_fields = ['name']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['university_name', 'start_date', 'end_date', 'grade']
    list_filter = ['start_date']
    search_fields = ['university_name']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'start_date', 'end_date', 'role']
    list_filter = ['company']
    search_fields = ['company', 'role']


class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'address', 'tel', 'email']
    list_filter = ['name']
    search_fields = ['name']


class SocialAdmin(admin.ModelAdmin):
    list_display = ['twitter', 'linkdin', 'skype', 'facebook', 'instagram']

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position')
    


# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Blog)
admin.site.register(PersonalInfo)
