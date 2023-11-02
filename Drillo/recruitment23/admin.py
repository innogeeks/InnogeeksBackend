
from django.contrib import admin
from .models import recruitments
from django.core.mail import send_mail, EmailMessage
from django.core import mail
from django.template.loader import render_to_string
import threading
from threading import Thread
from django.conf import settings

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, bcc=self.recipient_list)
        msg.content_subtype = "html"
        msg.send()

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()

class recruitmentsAdmin(admin.ModelAdmin):
    model = recruitments
    fields = ['name', 'email_personal', 'email_kiet', 'library_id', 'contact_no',
              'day_scholar_hosteller', 'gender', 'branch', 'payment_mode', 'desk', 'date', 'payment_status', 'recruitment_mail']

    list_display = ('name', 'payment_status', 'email_kiet', 'contact_no', 'id')

    list_per_page = 80

    list_filter = ('gender', 'day_scholar_hosteller', 'desk', 'payment_mode' ,'payment_status', 'date')

    search_fields = ('email_personal', 'email_kiet',
                     'name', 'contact_no', 'library_id')


    ordering = ('date', 'email_kiet')

    actions = ["send_confirmation_mail","send_test_slot_mail"]
   

    def send_confirmation_mail(self, request, queryset):
        connection = mail.get_connection()
        pl =[]
        for i in queryset:
            print(i.email_personal)
            if i.email_personal:
                pl.append(i.email_personal)
            # else:

        connection.open()
        message= render_to_string('confirmation.html')
        send_html_mail('Innogeeks Recruitment | Registration Successful',message,pl)

        connection.close()
        queryset.update(payment_status=True)
    send_confirmation_mail.short_description = "Send an email for due paymemt"
admin.site.register(recruitments, recruitmentsAdmin)