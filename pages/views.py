from django.shortcuts import render
from contact_us.models import ContactUs
from about.models import About, Service, Detail
from blog.models import Project, CurrentSite
from portfolio.models import Portfolio

# Create your views here.
def index1(request):
    about = About.objects.all()
    service = Service.objects.filter(show=True)
    detail = Detail.objects.all()

    project = Project.objects.order_by('-project_date').filter(show=True)
    currentSite = CurrentSite.objects.order_by('-current_project_date').filter(show=True)

    contact_us = ContactUs.objects.all()

    portfolio = Portfolio.objects.order_by('-project_date').filter(show=True)

    context = {
        "home_page" : "active",
        'contact_us' : contact_us,
        'about' : about,
        'service' : service,
        'detail': detail,
        'currentSite' : currentSite,
        'project' : project,
        'portfolio' : portfolio,
    }
    return render(request, 'pages/index.html', context)
