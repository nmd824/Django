from django import forms
from .models import MobileApp, AppPermissions


class MobileAppForm(forms.ModelForm):
    class Meta:
        model = MobileApp
        fields = ('name', 'icon', 'platform', 'type')


class AppPermissionForm(forms.ModelForm):
    class Meta:
        model = AppPermissions
        fields = ('mobile_app', 'type', 'reason', 'suggested', 'suggested_reason')
