from django.shortcuts import redirect

def login_required(view):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/auth/login/?status=403')
        return view(request, *args, **kwargs)
    return wrapper

