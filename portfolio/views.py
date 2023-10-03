from django.shortcuts import render, get_object_or_404
from contact_us.models import ContactUs
from .models import Portfolio
# Create your views here.
def portfolio(request):
    contact_us = ContactUs.objects.all()
    portfolio = Portfolio.objects.order_by('-project_date').filter(show=True)


    context = {
        'contact_us' : contact_us,
        'portfolio' : portfolio,
    }
    return render(request, 'portfolio/portfolio.html', context)

def project(request, project_id):
    portfolio = get_object_or_404(Portfolio, pk=project_id)

    contact_us = ContactUs.objects.all()


    context = {
        'contact_us' : contact_us,
        'portfolio' : portfolio,
        
    }
    return render(request, 'portfolio/project.html', context)