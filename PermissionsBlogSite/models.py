from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.
class MobileAppType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MobileApp(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='media/')
    platform_choices = [
        ('i', 'ios'),
        ('a', 'android'),
    ]
    platform = models.CharField(max_length=1, choices=platform_choices)
    type = models.ManyToManyField(MobileAppType, related_name='mobileapps')

    def __str__(self):
        return self.name

    # To get the name of the platform and not a single char
    def get_platform(self):
        return dict(MobileApp.platform_choices)[self.platform]


class AppPermissions(models.Model):
    mobile_app = models.ForeignKey(MobileApp, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    reason = models.TextField()

    suggested_choices = [

        (True, 'On'),
        (False, 'Off')
    ]

    suggested = models.BooleanField(choices=suggested_choices, default=True)
    suggested_reason = models.TextField()

    def __str__(self):
        return self.mobile_app.name

    # To get the name of the suggested choice and not a true / false
    def get_suggested_choice(self):
        return dict(AppPermissions.suggested_choices)[self.suggested]


class MobileAppUserConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_app = models.ForeignKey(MobileApp, on_delete=models.CASCADE)
    config = JSONField()

    def __str__(self):
        return self.user
