from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {'form':form}
    return render(request, 'contact.html', context)