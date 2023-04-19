from os import name
# from django.conf.urls import url
from django.db import models
from django .contrib.auth.models import User
from django.template.defaultfilters import date, default, slugify, title
from ckeditor.fields import RichTextField
import datetime
# from cloudinary.models import CloudinaryField

# Create your models here.


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name  = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default =80, blank=True, null= True)
    image = models.FileField(blank=True, null=True,upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_number =  models.IntegerField(default =80, blank=True, null= True)
    Freelance = models.BooleanField()

    about = models.TextField(blank=True, null= True)

    background = models.ImageField(blank=True, null= True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null= True)
    bio = models.TextField(blank=True, null= True)
    skills = models.ManyToManyField(Skill, blank=True)

    twitter = models.URLField(max_length=200, blank=True, null= True)
    facebook = models.URLField(max_length=200, blank=True, null= True)
    intergram = models.URLField(max_length=200, blank=True, null= True)
    linkedin = models.URLField(max_length=200, blank=True, null= True) 
    website = models.URLField(max_length=200, blank=True, null= True)
    # cv = models.FileField(blank=True, null= True, upload_to="cv")
    # cv = CloudinaryField(resource_type='', blank=True, null= True, unique_filename = False, use_filename = True)  


    def age_count(self):
        age = datetime.date.today().year - self.date_of_birth.year
        return age
        
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'




class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact profiles'
        verbose_name = 'Contact profile'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Message")
    
    def __str__(self):
        return f'{self.name}'



class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ['name']

    thumbnail = models.ImageField(blank=True, null= True, upload_to="thumbnail") 
    name = models.CharField(max_length=200,blank=True, null= True)
    role = models.CharField(max_length=200,blank=True, null= True) 
    quote = models.CharField(max_length=500,blank=True, null= True) 
    is_active = models.BooleanField(default = True) 

    def __str__(self):
        return self.name

class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ['name']

    image = models.ImageField(blank=True, null= True, upload_to="media")
    url = models.URLField(blank=True, null= True)
    name  =  models.CharField(max_length=200, blank=True, null= True )
    is_image = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False;
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio'
        verbose_name = 'Portfolio'
        ordering = ['name']

    date = models.DateTimeField(blank=True, null= True)
    name =models.CharField(max_length= 200 ,blank=True, null= True)
    description = models.CharField(max_length=500,blank=True, null= True)
    body= RichTextField(blank=True, null= True)
    image = models.ImageField(blank=True, null= True, upload_to="portfolio")
    slug = models.SlugField(blank=True, null= True)
    is_active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"
    


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'
    
    date =models.DateTimeField(blank=True, null= True)
    name = models.CharField(max_length= 50 ,blank=True, null= True)
    title = models.CharField(max_length= 200 ,blank=True, null= True) 
    description = models.CharField(max_length= 500 ,blank=True, null= True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name    



class Resume(models.Model):
    summary = models.TextField()
    work_experiences = models.ManyToManyField('WorkExperience')
    education = models.ManyToManyField('Education')
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return self.summary


class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.company_name


class Education(models.Model):
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.institution_name
