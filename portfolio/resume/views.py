from django.shortcuts import render
from .models import Skill, Education, Experience, Personal, Social, Testimonials, PersonalInfo
from .forms import MessageForm

# Create your views here.


def home(request):

    status = 200

    if request.method == "POST":
        print("POSTED DATA")
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            status = 201
        else:
            print("TELL them that sent data is not valid")

    messageForm = MessageForm()

    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    personal = Personal.objects.first()
    social = Social.objects.first()
    testimonial = Testimonials.objects.all()
    personal_info = PersonalInfo.objects.get(user__username = 'Ani')
    cntxt = {
             'skills': skills,
             'education': education,
             'experience': experience,
             'personal': personal,
             'social': social,
             'testimonial': testimonial,
             'personal_info': personal_info,
             "messageForm": messageForm
             }

    return render(request, 'index.html', context=cntxt, status=status)
