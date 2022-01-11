from django.contrib import messages
from django.conf import settings 
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def send_forget_password_mail(email , token ):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    print("send mail done")
    return True

def ChangePassword(request , token):
    context = {}
    try:
        context = {'user_id' : token}
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')     
            user_obj = User.objects.get(id = token)
            user_obj.set_password(new_password)
            user_obj.save()
            print('saving new password')
            return redirect('/login/')
            
    except Exception as e:
        print(e)
    return render(request , 'authenthicating/changePassword.html' , context)