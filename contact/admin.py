from django.contrib import admin
from .forms import ContactForm
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['sender', 'subject', 'message','timestamp']

admin.site.register(ContactForm, ContactFormAdmin)



# Register your models here.
