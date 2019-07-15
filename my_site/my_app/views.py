from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ilea1227@gmail.com',]
    send_mail( subject, message, email_from, recipient_list)
    # return redirect('redirect to a new page')

def index(request):
    if request.method =='POST':
        send_email(request)

    context = {}

    return render(request, 'index.html', context)



# def index(request):
#     return render(request, './src/index.html', context='')