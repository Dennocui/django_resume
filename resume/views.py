from django.shortcuts import render

# Create your views here.

from django.views import generic

class IndexView(generic.TemplateView):
     template_name = "index.html"

    #  def get_context_data(self, **kwargs):

        
    #     return  context

    #      context = super().get_context_data(**kwargs)

    #      testimonials = Testimonial.objects.filter(is_active=True)
    #      certificates = Certificate.objects.filter(is_active=True).order_by("-date")
    #      blogs = Blog.objects.filter(is_active=True).order_by("-timestamp")
    #      portfolio = Portfolio.objects.filter(is_active=True).order_by("-date")

    #      context["testimonials"] = testimonials
    #      context["certificates"] = certificates
    #      context["blogs "] = blogs 
    #      context["portfolio"] = portfolio

    #      return  context