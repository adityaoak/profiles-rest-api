from django.contrib import admin
from profiles_api import models  #import our custom class

# Register your models here.
admin.site.register(models.UserProfile)
