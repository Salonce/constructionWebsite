from django.http import HttpResponse
from django.shortcuts import redirect


def authGoHome(view_func):
    def redirectToHome(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return redirectToHome


def onlyAuthPermitted(view_func):
    def redirectToLoginPage(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('loginPage')
        else:
            return view_func(request, *args, **kwargs)

    return redirectToLoginPage


def allowOnlySpecificRoles(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Not allowed to be here')
        return wrapper
    return decorator
