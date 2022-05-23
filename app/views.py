from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    send_mail('Subject here', 'Here is the message.', 'send email', ['your email'], fail_silently=False)
    return render(request, 'home.html')