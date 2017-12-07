from django.contrib import admin

# Register your models here.
from .models import Profile

class profileAdmin(admin.ModelAdmin):
    """Creates a model in the database allowing you to
     manage the data from the database's Admin panel"""
    class Meta:
        """Specifies the name of the model in the Admin panel"""
        model = Profile

admin.site.register(Profile, profileAdmin)
