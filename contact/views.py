from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm
from home.forms import SignUpForm
from shop.models import Category


def contact(request):
    template = 'contact/contact.html'
    categories = Category.objects.all()
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST or None)
        form = ContactForm(request.POST or None)
        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
            sign_up_form.save()
            return HttpResponseRedirect('/contact/')
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            form.save()
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
        sign_up_form = SignUpForm()
    context = {'form': form,
               'sign_up_form':sign_up_form,
               'categories': categories,
               }
    return render(request, template, context)
