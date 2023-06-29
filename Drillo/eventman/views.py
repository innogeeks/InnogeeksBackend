from django.conf import settings
from django.contrib import admin
from importlib import import_module, reload
from rest_framework.decorators import api_view
from django.urls import clear_url_caches
from dynamic_models.models import FieldSchema, ModelSchema
from django.shortcuts import render, redirect
from .forms import FormSubmissionForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponse

@csrf_exempt
def form_submission(request):
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.save()
            model = MyDynamicModel(submission.name)
            url = submission.url
            return redirect(reverse('page_preview', kwargs={'url': url}))

    else:
        form = FormSubmissionForm()
    return render(request, 'create.html', {'form': form})

def page_preview(request,url):
    submission = FormSubmission.objects.get(url=url)
    return render(request, 'rendered-page.html', {'submission': submission})

def MyDynamicModel(modelName):
    try:
        model_schema = ModelSchema.objects.create(
            name=modelName)
    except Exception as e:
        return ("exists")
    field_schema = FieldSchema.objects.create(
        name="name",
        data_type="character",
        model_schema=model_schema,
        max_length=200,
        )
    model_create = Modelnames.objects.create(
        modelname=modelName)
    reg_model = model_schema.as_model()
    admin.site.register(reg_model)
    reload(import_module(settings.ROOT_URLCONF))
    clear_url_caches()
    return ("created successfully")
