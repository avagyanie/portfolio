from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    
    def __str__(self) -> str:
        return f"Name is {self.name}, value is {self.value}"


class Education(models.Model):
    grade = models.TextField(max_length=30, blank=True, null=True)
    start_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    university_name = models.TextField(max_length=70)

    def __str__(self) -> str:
        return f"Grade - {self.grade}, university_name - {self.university_name}"


class Experience(models.Model):
    role = models.TextField(max_length=30)
    start_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    company = models.TextField(max_length=70)
    description1 = models.CharField(max_length = 200)
    description2 = models.CharField(max_length = 200)
    description3 = models.CharField(max_length = 200)
    description4 = models.CharField(max_length = 200)
    
    def __str__(self) -> str:
        return f"Role - {self.role}, company - {self.company}"

class Personal(models.Model):
    name = models.TextField(max_length=12)
    surname = models.TextField(max_length=12)
    address = models.TextField(max_length=30)
    tel = models.CharField(max_length=12)
    web = models.TextField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    birthday = models.DateField()
    city = models.TextField(max_length=12)
    title = models.TextField(max_length=21)
    degree = models.TextField(max_length=10)
    text1 = models.TextField(max_length=100)
    text2 = models.TextField(max_length=200)
    text3 = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add= True)

    def yearpublished(self):
        return self.pub_date.strftime('%Y')
    
    def __str__(self) -> str:
        return f"Name - {self.name}, surname - {self.surname}"


class Social(models.Model):
    github = models.TextField(max_length=70, default='a')
    linkedin = models.TextField(max_length=70, default='a')
    telegram = models.TextField(max_length=70, default='a')

    def __str__(self) -> str:
        return f"Social pages"

class Testimonials(models.Model):
    full_name = models.TextField(max_length=30)
    position = models.TextField(max_length=70)
    testimonial = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images/')
    link = models.URLField()
    

    def __str__(self) -> str:
        return f"Name - {self.full_name}"
    

class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Message(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.full_name


class PortfolioProject(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    url = models.URLField()


    def __str__(self) -> str:
        return self.name
    