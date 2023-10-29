from django.contrib import admin
from .models import recruitments
from django.core.mail import send_mail


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
        subject = "Registration Successful"
        message = "Congratulations!! We recieved your details, we'll contact you soon✅"
        from_email = 'neha.2125csit1004@kiet.edu'

        for item in queryset:
            recipient = item.email_personal

            send_mail(subject, message, from_email, [recipient])
        queryset.update(payment_status=True)
    send_confirmation_mail.short_description = "Send Confirmation Mail to selected users."


# Register your models here.
admin.site.register(recruitments, recruitmentsAdmin)
