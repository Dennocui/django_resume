from django.shortcuts import render
from django.contrib import messages
from . models import UserProfile, Portfolio, Testimonial, Certificate

from django.views import generic

# from . forms import ContactForm


class IndexView(generic.TemplateView):
     template_name = "index.html"

     def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True).order_by("-date")
        # blogs = Blog.objects.filter(is_active=True).order_by("-timestamp")
        portfolio = Portfolio.objects.filter(is_active=True).order_by("-date")

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        # context["blogs "] = blogs 
        context["portfolio"] = portfolio

        return  context