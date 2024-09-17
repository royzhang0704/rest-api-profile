from django.contrib import admin
from api_profile import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
