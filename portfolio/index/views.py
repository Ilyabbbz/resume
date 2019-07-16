from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings
from portfolio.config import EMAIL


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def email(request):

    subject = request.POST['subject']
    message = request.POST['username'] +'\n'+ request.POST['message'] +'\n'+ request.POST['phone'] +'\n'+ request.POST['mailadr']
    email_from = EMAIL
    recipient_list = ['ilyabbbz@gmail.com', ]

    send_mail(subject, message, email_from, recipient_list)

    print(request.POST)
    return redirect('index')