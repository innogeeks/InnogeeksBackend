from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate,  login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@csrf_exempt
def signup(request):
    msg = ""
    error_fields = []
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'User created successfully.')
            return redirect("login_view")
        else:
            for field, errors in form.errors.items():
                error_fields.append(field)
            print("Form errors:", form.errors)
            if "password2" in error_fields:
                msg = "Password is too weak or password does not match confirm password"
            else:
                msg = "Error in form submission"
            print("Error message:", msg)
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form, 'msg': msg})

@csrf_exempt
def login(request):
    msg = None
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if(form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if(user is not None):
                auth_login(request, user)
                return redirect('dashboard')
            else:
                msg = "invalid credentials"
        else:
            msg = "error in validating form"
    return render(request, "login.html", {'form': form, 'msg': msg})


def logout(request):
    auth_logout(request)
    return redirect("login_view")

# def dashboard(request):
#     if (request.user.is_authenticated):
#         user = User.objects.get(username=request.user)
#         if(user.is_coordinator):
#             return render(request, "coordinatorDash.html", {"user": user, 'created': user.events_created.split(), 'length': len(user.events_created.split()), 'range': range(len(user.events_created.split()))})
#         else:
#             return render(request, "studentDash.html", {"user": user, 'participated': user.events_participated.split(), 'length': len(user.events_participated.split()), 'range': range(len(user.events_participated.split()))})
#     else:
#         return redirect('login_view')
@login_required
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        if user.is_coordinator:
            return render(
                request,
                "coordinatorDash.html",
                {
                    "user": user,
                    "created": user.events_created.split(),
                    "length": len(user.events_created.split()),
                    "range": range(len(user.events_created.split())),
                },
            )
        else:
            return render(
                request,
                "studentDash.html",
                {
                    "user": user,
                    "participated": user.events_participated.split(),
                    "length": len(user.events_participated.split()),
                    "range": range(len(user.events_participated.split())),
                },
            )
    else:
        return redirect("login_view")

