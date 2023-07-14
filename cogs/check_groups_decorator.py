from django.shortcuts import render

def validate_user_in_group(*groups):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return function(request, *args, **kwargs)
            
            return render(request,"404.html")
        
        return wrapper
    
    return decorator