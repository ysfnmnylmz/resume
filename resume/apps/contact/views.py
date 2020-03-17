from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm


@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse([{'status': 'success', 'text': 'Thank you for your message!'}],
                                safe=False)
        else:
            return JsonResponse([{'status': 'warning', 'text': form.errors}], safe=False)
