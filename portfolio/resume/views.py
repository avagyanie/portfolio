from django.shortcuts import render
from .models import Skill, Education, Experience, Personal, Social, Testimonials, PersonalInfo, PortfolioProject
from .forms import MessageForm
from django.shortcuts import get_object_or_404

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
    portfolio_project = PortfolioProject.objects.all()
    cntxt = {
             'skills': skills,
             'education': education,
             'experience': experience,
             'personal': personal,
             'social': social,
             'testimonial': testimonial,
             'personal_info': personal_info,
             "messageForm": messageForm,
             "portfolio_project": portfolio_project,
             }

    return render(request, 'index.html', context=cntxt, status=status)


def portfolio_project(request, id):
    project = get_object_or_404(PortfolioProject, id=id)
    return render(request, 'portfolio-details.html', context= {"project": project})
