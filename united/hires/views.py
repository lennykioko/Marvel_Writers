"""Handles the different views of the hire page"""
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from profiles.models import Profile
from .forms import Hireform

# Create your views here.
def hire(request):
    """Displays the hire form or validates user input and sends this data via email.
     It also displays the calculated cost. Either occurs depending on the type of request
    """
    title = 'Hire Us'
    form = Hireform(request.POST or None)
    confirm_order = None
   
    if form.is_valid():
        Subject_Category = form.cleaned_data['Subject_Category']
        Subject_Area = form.cleaned_data['Subject_Area']
        Document_Type = form.cleaned_data['Document_Type']
        topic = form.cleaned_data['topic']
        Academic_Level = form.cleaned_data['Academic_Level']
        Number_of_Pages = form.cleaned_data['Number_of_Pages']
        Spacing = form.cleaned_data['Spacing']
        Style = form.cleaned_data['Style']
        Number_of_Sources_or_References = form.cleaned_data['Number_of_Sources_or_References']
        Preffered_Language = form.cleaned_data['Preffered_Language']
        Urgency = form.cleaned_data['Urgency']
        Preffered_Writer = form.cleaned_data['Preffered_Writer']
        Description_or_instructions = form.cleaned_data['Description_or_instructions']
        Firstname = form.cleaned_data['Firstname']
        Lastname = form.cleaned_data['Lastname']
        Email = form.cleaned_data['Email']
        Country = form.cleaned_data['Country']
        Contact_Phone = form.cleaned_data['Contact_Phone']

        subject = 'NEW CLIENT ORDER (%s)' % (Firstname)

        message = """SUBJECT_CATEGORY = %s\n 
                     SUBJECT_AREA  = %s\n 
                     DOCUMENT_TYPE = %s\n 
                     TOPIC = %s\n 
                     ACADEMIC_LEVEL  = %s\n 
                     NUMBER_OF_PAGES = %s\n 
                     SPACING = %s\n 
                     STYLE = %s\n
                     NUMBER_OF_SOURCES_OR_REFERENCES = %s\n 
                     PREFFERED_LANGUAGE = %s\n 
                     URGENCY = %s\n 
                     PREFFERED_WRITER = %s\n
                     DESCRIPTION_OR_INSTRUCTIONS = %s\n 
                     FIRSTNAME     = %s\n 
                     LASTNAME = %s\n 
                     EMAIL = %s\n
                     COUNTRY = %s\n 
                     CONTACT_PHONE = %s""" %(Subject_Category, Subject_Area, Document_Type, topic, 
                                                Academic_Level, Number_of_Pages, Spacing, Style,
                                                Number_of_Sources_or_References, Preffered_Language, Urgency, 
                                                Preffered_Writer, Description_or_instructions, 
                                                Firstname, Lastname, Email, Country, Contact_Phone,)
        
        emailFrom = form.cleaned_data['Email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        
        title = "Confirm Order"

        cpp = 0

        if Urgency == '1 month' and Academic_Level == 'High school':
            cpp = 10
        elif Urgency == '1 month' and Academic_Level == 'College':
            cpp = 11
        elif Urgency == '1 month' and Academic_Level == 'University':
            cpp = 12
        elif Urgency == '1 month' and Academic_Level == 'Masters':
            cpp = 13
        elif Urgency == '1 month' and Academic_Level == 'PhD':
            cpp = 14
        
        elif Urgency == 'Longer(kindly specify in description)' and Academic_Level == 'High school':
            cpp = 10
        elif Urgency == 'Longer(kindly specify in description)' and Academic_Level == 'College':
            cpp = 11
        elif Urgency == 'Longer(kindly specify in description)' and Academic_Level == 'University':
            cpp = 12
        elif Urgency == 'Longer(kindly specify in description)' and Academic_Level == 'Masters':
            cpp = 13
        elif Urgency == 'Longer(kindly specify in description)' and Academic_Level == 'PhD':
            cpp = 14

        elif Urgency == '3 Weeks' and Academic_Level == 'High school':
            cpp = 11
        elif Urgency == '3 Weeks' and Academic_Level == 'College':
            cpp = 12
        elif Urgency == '3 Weeks' and Academic_Level == 'University':
            cpp = 13
        elif Urgency == '3 Weeks' and Academic_Level == 'Masters':
            cpp = 14
        elif Urgency == '3 Weeks' and Academic_Level == 'PhD':
            cpp = 15

        elif Urgency == '2 Weeks' and Academic_Level == 'High school':
            cpp = 12
        elif Urgency == '2 Weeks' and Academic_Level == 'College':
            cpp = 13
        elif Urgency == '2 Weeks' and Academic_Level == 'University':
            cpp = 14
        elif Urgency == '2 Weeks' and Academic_Level == 'Masters':
            cpp = 15
        elif Urgency == '2 Weeks' and Academic_Level == 'PhD':
            cpp = 16

        elif Urgency == '10 Days' and Academic_Level == 'High school':
            cpp = 13
        elif Urgency == '10 Days' and Academic_Level == 'College':
            cpp = 14
        elif Urgency == '10 Days' and Academic_Level == 'University':
            cpp = 15
        elif Urgency == '10 Days' and Academic_Level == 'Masters':
            cpp = 16
        elif Urgency == '10 Days' and Academic_Level == 'PhD':
            cpp = 17

        elif Urgency == '1 Week(7 days)' and Academic_Level == 'High school':
            cpp = 14
        elif Urgency == '1 Week(7 days)' and Academic_Level == 'College':
            cpp = 15
        elif Urgency == '1 Week(7 days)' and Academic_Level == 'University':
            cpp = 16
        elif Urgency == '1 Week(7 days)' and Academic_Level == 'Masters':
            cpp = 17
        elif Urgency == '1 Week(7 days)' and Academic_Level == 'PhD':
            cpp = 18
        
        elif Urgency == '5 Days' and Academic_Level == 'High school':
            cpp = 15
        elif Urgency == '5 Days' and Academic_Level == 'College':
            cpp = 16
        elif Urgency == '5 Days' and Academic_Level == 'University':
            cpp = 17
        elif Urgency == '5 Days' and Academic_Level == 'Masters':
            cpp = 18
        elif Urgency == '5 Days' and Academic_Level == 'PhD':
            cpp = 19

        elif Urgency == '4 Days' and Academic_Level == 'High school':
            cpp = 16
        elif Urgency == '4 Days' and Academic_Level == 'College':
            cpp = 17
        elif Urgency == '4 Days' and Academic_Level == 'University':
            cpp = 18
        elif Urgency == '4 Days' and Academic_Level == 'Masters':
            cpp = 19
        elif Urgency == '4 Days' and Academic_Level == 'PhD':
            cpp = 20

        elif Urgency == '3 Days' and Academic_Level == 'High school':
            cpp = 17
        elif Urgency == '3 Days' and Academic_Level == 'College':
            cpp = 18
        elif Urgency == '3 Days' and Academic_Level == 'University':
            cpp = 19
        elif Urgency == '3 Days' and Academic_Level == 'Masters':
            cpp = 20
        elif Urgency == '3 Days' and Academic_Level == 'PhD':
            cpp = 21

        elif Urgency == '2 Days' and Academic_Level == 'High school':
            cpp = 18
        elif Urgency == '2 Days' and Academic_Level == 'College':
            cpp = 19
        elif Urgency == '2 Days' and Academic_Level == 'University':
            cpp = 20
        elif Urgency == '2 Days' and Academic_Level == 'Masters':
            cpp = 21
        elif Urgency == '2 Days' and Academic_Level == 'PhD':
            cpp = 22

        elif Urgency == '24 Hours' and Academic_Level == 'High school':
            cpp = 19
        elif Urgency == '24 Hours' and Academic_Level == 'College':
            cpp = 20
        elif Urgency == '24 Hours' and Academic_Level == 'University':
            cpp = 21
        elif Urgency == '24 Hours' and Academic_Level == 'Masters':
            cpp = 22
        elif Urgency == '24 Hours' and Academic_Level == 'PhD':
            cpp = 23

        elif Urgency == '12 Hours' and Academic_Level == 'High school':
            cpp = 20
        elif Urgency == '12 Hours' and Academic_Level == 'College':
            cpp = 21
        elif Urgency == '12 Hours' and Academic_Level == 'University':
            cpp = 22
        elif Urgency == '12 Hours' and Academic_Level == 'Masters':
            cpp = 23
        elif Urgency == '12 Hours' and Academic_Level == 'PhD':
            cpp = 24
        
        elif Urgency == '6 Hours' and Academic_Level == 'High school':
            cpp = 21
        elif Urgency == '6 Hours' and Academic_Level == 'College':
            cpp = 22
        elif Urgency == '6 Hours' and Academic_Level == 'University':
            cpp = 23
        elif Urgency == '6 Hours' and Academic_Level == 'Masters':
            cpp = 24
        elif Urgency == '6 Hours' and Academic_Level == 'PhD':
            cpp = 25

        elif Urgency == '3 Hours' and Academic_Level == 'High school':
            cpp = 22
        elif Urgency == '3 Hours' and Academic_Level == 'College':
            cpp = 23
        elif Urgency == '3 Hours' and Academic_Level == 'University':
            cpp = 24
        elif Urgency == '3 Hours' and Academic_Level == 'Masters':
            cpp = 25
        elif Urgency == '3 Hours' and Academic_Level == 'PhD':
            cpp = 26

        else:
            cpp = 0

        Cost = int(Number_of_Pages) * cpp
        confirm_order = "Total Cost: %s USD" % (Cost)

        db_data = Profile.objects.create(name=Firstname, email=Email, cost=Cost)

        form = None
    
    context = {'title': title, 'form': form, 'confirm_order': confirm_order}

    template = 'hire.html'
    return render(request, template, context)
