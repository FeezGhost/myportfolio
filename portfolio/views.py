from django.shortcuts import render

from django.core.mail import send_mail

# Create your views here.
def homepage(request):
    if request.method == "POST":
        message = request.POST['message']
        sender_email = request.POST['email']
        first_name =  request.POST['fname']
        last_name = request.POST['lname']
        subject = first_name + last_name
        message = message + ' ' + sender_email
        send_mail(
            subject,
            message,
            sender_email,
            ['hussainnaqvi106@gmail.com']
        )
        return render(request, 'portfolio/index.html', {'subject':subject})

    return render(request, 'portfolio/index.html', {})
