from django.contrib import admin
from .models import MobileApp
from .models import MobileAppType
from .models import AppPermissions
from .models import MobileAppUserConfig

# Register your models here.
admin.site.register(MobileApp)
admin.site.register(MobileAppType)
admin.site.register(AppPermissions)
admin.site.register(MobileAppUserConfig)
