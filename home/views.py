from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from shop.models import Category


def home(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST or None)
        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
            sign_up_form.save()
            return HttpResponseRedirect('/home/')

    else:
        sign_up_form = SignUpForm()
    context = {
        'sign_up_form': sign_up_form,
        'categories': categories,
    }
    return render(request, 'home/home.html', context)
