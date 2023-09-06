from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def unauthentication_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('driver_page')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return render(request, 'hospital/404.html')
            else:
                return render(request, 'hospital/404.html')
        return wrapper_func
    return decorator 