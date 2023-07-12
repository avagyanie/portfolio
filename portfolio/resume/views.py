from django.shortcuts import render
from .models import Skill, Education, Experience, Personal, Social, Testimonials

# Create your views here.


def home(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    personal = Personal.objects.first()
    social = Social.objects.first()
    testimonial = Testimonials.objects.all()
    cntxt = {
             'skills': skills,
             'education': education,
             'experience': experience,
             'personal': personal,
             'social': social,
             'testimonial': testimonial,
             }

    return render(request, 'index.html', context=cntxt)
