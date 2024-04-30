from django.shortcuts import render, redirect
from website.forms import ContactForm


def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('website_thank_you')
        
    context = { 'form':form }
    return render(request, 'website/pages/index.html', context=context)

def portfolio_details(request):
    context = {}
    return render(request, 'website/pages/portfolio-details.html', context=context)


def django_filters(request):
    context = {'number':10}
    return render(request, 'filter.html',context=context)


def thank_you(request):
    return render(request, 'website/pages/thank_you.html')