from django.shortcuts import render
from .models import Skill, Education, Experience, Personal, Social, Testimonials, Blog, PersonalInfo

# Create your views here.


def home(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    personal = Personal.objects.first()
    social = Social.objects.first()
    testimonial = Testimonials.objects.all()
    blogs = Blog.objects.filter(user__username="admin")
    personal_info = PersonalInfo.objects.get(user__username = 'Ani')
    cntxt = {
             'skills': skills,
             'education': education,
             'experience': experience,
             'personal': personal,
             'social': social,
             'testimonial': testimonial,
             'blogs': blogs,
             'personal_info': personal_info,
             }

    return render(request, 'index.html', context=cntxt)

def blog(request):
    
    return render(request, 'blog.html')
