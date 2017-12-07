"""Creates form fields for crispy forms"""
from django import forms

#document field with a dropdown menu
DOCUMENT = [  
    ('Not Sure', 'Not Sure'),
    ('An Essay', 'An Essay'),
    ('Article', 'Article'),
    ('Math Problem', 'Math Problem'),
    ('Economic Assignment', 'Economic Assignment'),
    ('Homework', 'Homework'),
    ('Speech_or_Presentation', 'Speech_or_Presentation'),
    ('Term Paper', 'Term Paper'),
    ('Critique Essay', 'Critique Essay'),
    ('PowerPoint', 'PowerPoint'),
    ('Application_or_Admission Essay', 'Application_or_Admission Essay'),
    ('Article Critique', 'Article Critique'),
    ('Research Paper', 'Research Paper'),
    ('Course Work', 'Course Work'),
    ('Book Report', 'Book Report'),
    ('Book Review', 'Book Review'),
    ('Movie Review', 'Movie Review'),
    ('Personal Statement', 'Personal Statement'),
    ('Proofreading', 'Proofreading'),
    ('Thesis', 'Thesis'),
    ('Thesis Proposal', 'Thesis Proposal'),
    ('Research Proposal', 'Research Proposal'),
    ('Dissertation', 'Dissertation'),
    ('Dissertation Chapter - Abstract', 'Dissertation Chapter - Abstract'),
    ('Dissertation Chapter - Introduction', 'Dissertation Chapter - Introduction'),
    ('Dissertation Chapter - List Review', 'Dissertation Chapter - List Review'),
    ('Dissertation Chapter - Methodology', 'Dissertation Chapter - Methodology'),
    ('Dissertation Chapter - Results', 'Dissertation Chapter - Results'),
    ('Dissertation Chapter - Discussion', 'Dissertation Chapter - Discussion'),
    ('Dissertation Chapter - Editing', 'Dissertation Chapter - Editing'),
    ('Dissertation Chapter - ProofReading', 'Dissertation Chapter - ProofReading'),
    ('Annotated Bibliography', 'Annotated Bibliography'),
    ('Formatting', 'Formatting'),
    ('Editing', 'Editing'),
    ('Capstone Project', 'Capstone Project'),
    ('SEO Articles', 'SEO Articles'),
    ('Lab Report', 'Lab Report'),
    ('Business Plan', 'Business Plan'),
]

PAGES = [(x, x) for x in range(1, 251)]

SPACING = [
    ("Double Spaced", "Double Spaced"),
    ("Single Spaced", "Single Spaced"),
]

LEVEL = [
    ('High school', 'High school'),
    ('College', 'College'),
    ('University', 'University'),
    ('Masters', 'Masters'),
    ('PhD', 'PhD'),
]

URGENCY = [
    ('3 Hours', '3 Hours'),
    ('6 Hours', '6 Hours'),
    ('12 Hours', '12 Hours'),
    ('24 Hours', '24 Hours'),
    ('2 Days', '2 Days'),
    ('3 Days', '3 Days'),
    ('4 Days', '4 Days'),
    ('5 Days', '5 Days'),
    ('1 Week(7 days)', '1 Week(7 days)'),
    ('10 Days', '10 Days'),
    ('2 Weeks', '2 Weeks'),
    ('3 Weeks', '3 Weeks'),
    ('1 month', '1 month'),
    ('Longer(kindly specify in description)', 'Longer(kindly specify in description)'),
]

SUBJECT = [
    ("NOT SURE", "NOT SURE"),
    ("HOMEWORK/ASSIGNMENT", "HOMEWORK/ASSIGNMENT"),
    ("LITERATURE AND LANGUAGE", "LITERATURE AND LANGUAGE"),
    ("SOCIAL SCIENCES", "SOCIAL SCIENCES"),
    ("HISTORY", "HISTORY"),
    ("LAW", "LAW"),
    ("MATHEMATICS AND ECONOMICS", "MATHEMATICS AND ECONOMICS"),
    ("TECHNOLOGY", "TECHNOLOGY"),
    ("NATURE", "NATURE "),
    ("EDUCATION", "EDUCATION"),
    ("HEALTH AND MEDICINE", "HEALTH AND MEDICINE"),
    ("COMMUNICATIONS AND MEDIA", "COMMUNICATIONS AND MEDIA"),
    ("RELIGION AND THEOLOGY", "RELIGION AND THEOLOGY"),
    ("LIFE SCIENCES", "LIFE SCIENCES"),
    ("TOURISM", "TOURISM"),
    ("CREATIVE WRITING", "CREATIVE WRITING"),
]

STYLE = [
    ("Not Sure", "Not Sure"),
    ("APA", "APA"),
    ("MLA", "MLA"),
    ("Chicago", "Chicago"),
    ("Harvard", "Harvard"),
    ("Turabian", "Turabian"),
]

REFRENCES = [(x, x) for x in range(0, 51)]

LANGUAGE = [
    ("English US", "English US"),
    ("Not a native speaker", "Not a native speaker"),
]


class Hireform(forms.Form):
    """Creates the actual fields for the form using the above variables for the dropdowns"""
    Subject_Category = forms.ChoiceField(required=True, choices=SUBJECT, widget=forms.Select())
    Subject_Area = forms.CharField(required=True, max_length=100)
    Document_Type = forms.ChoiceField(required=True, choices=DOCUMENT, widget = forms.Select())
    topic = forms.CharField(required=True, max_length=200)

    Academic_Level = forms.ChoiceField(required=True, choices=LEVEL, widget=forms.Select())
    Number_of_Pages = forms.ChoiceField(required=True, choices=PAGES, widget=forms.Select())
    Spacing = forms.ChoiceField(required=True, choices=SPACING, widget=forms.Select())
    Style = forms.ChoiceField(required=True, choices=STYLE, widget=forms.Select())

    Number_of_Sources_or_References = forms.ChoiceField(required=True, choices=REFRENCES,
                                                         widget=forms.Select())
    Preffered_Language = forms.ChoiceField(required=True, choices=LANGUAGE, widget=forms.Select())
    Urgency = forms.ChoiceField(required=True, choices=URGENCY, widget=forms.Select())

    Preffered_Writer = forms.CharField(required=False, max_length=100)
    Description_or_instructions = forms.CharField(required=False, widget=forms.Textarea)

    Firstname = forms.CharField(required=True, max_length=50)
    Lastname = forms.CharField(required=True, max_length=50)
    Email = forms.EmailField(required=True)
    Country = forms.CharField(required=True, max_length=50)
    Contact_Phone = forms.CharField(required=False, max_length=100)
