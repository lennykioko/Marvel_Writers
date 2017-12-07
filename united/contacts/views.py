"""Creates the different views for the contact page"""
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def contact(request):
    """Displays the contact form or validates user input before sending it via email 
    and then displays the confirmation message. Either occurs depending on the type of request
    """
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        subject = 'NEW CLIENT MESSAGE (%s)' % (name)
        message = '%s \n %s \n %s' %(name, email, comment)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message, we will get right back to you"
        form = None
        
    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = 'contact.html'
    return render(request, template, context)
