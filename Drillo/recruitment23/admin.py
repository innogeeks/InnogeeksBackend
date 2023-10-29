from django.contrib import admin
from .models import recruitments
from django.core.mail import send_mail, EmailMessage
from django.core import mail
from django.template.loader import render_to_string
import threading
from threading import Thread

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()

class recruitmentsAdmin(admin.ModelAdmin):
    model = recruitments
    fields = ['name', 'email_personal', 'email_kiet', 'library_id', 'contact_no',
              'day_scholar_hosteller', 'gender', 'branch', 'payment_mode', 'desk', 'date', 'payment_status']

    list_display = ('name', 'payment_status', 'email_kiet', 'contact_no')

    list_per_page = 80

    list_filter = ('gender', 'day_scholar_hosteller', 'desk', 'payment_mode')

    search_fields = ('email_personal', 'email_kiet',
                     'name', 'contact_no', 'library_id')

    ordering = ('date', 'email_kiet')

    actions = ["send_confirmation_mail"]

    def send_confirmation_mail(self, request, queryset):
        connection = mail.get_connection()
        # connection.open()
        pl =[]
        pl2=[]
        for i in queryset:
            print(i.email_personal)
            if i.email_personal:
                pl.append(i.email_personal)
            if i.email_kiet:
                pl2.append(i.email_kiet)
            # else:

        connection.open()
        message= render_to_string('confirmation.html')
        send_html_mail('Innogeeks Recruitment | Due Payment',message,pl) 
        send_html_mail('Innogeeks Recruitment | Due Payment',message,pl2)

        connection.close()
    send_confirmation_mail.short_description = "Send an email for due paymemt"


















    #     subject = "Registration Successful"
    #     message = "Congratulations!! We recieved your details, we'll contact you soon✅"
    #     from_email = 'neha.2125csit1004@kiet.edu'

    #     for item in queryset:
    #         recipient = item.email_personal

    #         send_mail(subject, message, from_email, [recipient])
    #     queryset.update(payment_status=True)
    # send_confirmation_mail.short_description = "Send Confirmation Mail to selected users."


# Register your models here.
admin.site.register(recruitments, recruitmentsAdmin)
