from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField, ArrayField


# Create your models here.
class MobileAppType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MobileApp(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='media/')
    platform_choices = [
        ('ios', 'ios'),
        ('android', 'android'),
    ]
    platform = ArrayField(ArrayField(
            models.CharField(max_length=7, blank=True),
            size=2,
        ),
        size=2,)
    type = models.ManyToManyField(MobileAppType, related_name='mobileapps')

    def __str__(self):
        return self.name


class PermType(models.Model):
    name = models.CharField(max_length=200)
    platform_choices = [
        ('ios', 'ios'),
        ('android', 'android'),
    ]
    platform = ArrayField(ArrayField(
        models.CharField(max_length=7, blank=True),
        size=2,
    ),
        size=2,)

    def __str__(self):
        return self.name


class AppPermissions(models.Model):
    mobile_app = models.ForeignKey(MobileApp, on_delete=models.CASCADE)
    type = models.ForeignKey(PermType, on_delete=models.CASCADE)
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
