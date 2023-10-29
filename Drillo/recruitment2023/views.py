from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def forms(request):
    return render(request, 'recruitment2023.html')
def submit(request):
    if request.method == 'POST':
        name = request.POST.get("Name", "") 
        email_personal = request.POST.get("Personal-Email", "")
        email_kiet = request.POST.get("College-Email", "")
        library_id = request.POST.get("Library-ID", "")
        contact_no = request.POST.get("Contact", "")
        branch = request.POST.get("Branch", "")
        gender = request.POST.get("Gender", "")
        payment_mode = request.POST.get("Payment", "")
        day_scholar_hosteller = request.POST.get("Residence", "")
        desk = request.POST.get("Desk", "")

        if recruitments.objects.filter(email_kiet=email_kiet).exists():
            messages.error(request, "Email Id already exists!!")
        else:
            new_reg = recruitments(
                name=name,
                email_personal=email_personal,
                email_kiet=email_kiet,
                library_id=library_id,
                contact_no=contact_no,
                branch=branch,
                gender=gender,
                payment_mode=payment_mode,
                day_scholar_hosteller=day_scholar_hosteller,
                desk=desk,
            )

            new_reg.save()
            # messages.success(request, "Registered Successfully")
            return render(request, "submitted.html")
    else:
        return redirect("") 
    return render(request, 'recruitment2023.html')