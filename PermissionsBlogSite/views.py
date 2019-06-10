from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import MobileAppForm, AppPermissionForm
from .models import MobileApp, AppPermissions


# Create your views here.
def index(request):
    template_name = 'index.html'
    context = {"header": 'Permissions Blog Site'}
    return render(request, template_name, context)


def create_app_form(request):
    template_name = 'create_app_form.html'
    form = MobileAppForm(request.POST or None, request.FILES)
    if form.is_valid():
        messages.success(request, 'Successfully stored Mobile App')
        form.save()
        form = MobileAppForm()
    context = {
        "header": 'Create Mobile App Form',
        "form": form,
    }
    return render(request, template_name, context)


def create_app_permission_form(request):
    template_name = 'create_permission_form.html'
    form = AppPermissionForm(request.POST or None)
    if form.is_valid():
        messages.success(request, 'Successfully stored App Permission')
        form.save()
        form = AppPermissionForm()
    context = {
        "header": 'Create App Permission Form',
        "form": form,
    }
    return render(request, template_name, context)


def view_all_app(request):
    template_name = 'view_all_apps.html'
    mobile_app_list = MobileApp.objects.all()
    context = {

        "header": 'View All Mobile App',
        "mobile_app_list": mobile_app_list
    }
    return render(request, template_name, context)


def view_permission(request):
    template_name = 'view_permissions.html'
    permission_list = AppPermissions.objects.all()
    context = {

        "header": 'View All App Permissions',
        "permission_list": permission_list
    }
    return render(request, template_name, context)


def edit_permission(request, pk):
    template_name = 'edit_permission.html'
    permission = get_object_or_404(AppPermissions, pk=pk)
    form = AppPermissionForm(request.POST, instance=permission)
    if form.is_valid():
        messages.success(request, 'Successfully edited App Permission')
        form.save()
    context = {

        "header": 'Edit App Permissions',
        "form": form
    }
    return render(request, template_name, context)
