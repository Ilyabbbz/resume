from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


# def email(request):

#     subject =
