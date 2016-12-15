from django.contrib import admin
from home.forms import SignUpForm
from home.models import SignUpForm


class SignUpFormAdmin(admin.ModelAdmin):
    list_display = ['email', 'created']


admin.site.register(SignUpForm, SignUpFormAdmin)
