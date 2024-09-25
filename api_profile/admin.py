from django.contrib import admin
from api_profile import models

# Register my models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
