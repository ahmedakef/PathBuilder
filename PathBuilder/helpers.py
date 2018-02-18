import hashlib
from django.utils.crypto import get_random_string
from django.conf import settings    
from django.core.mail import send_mail
from smtplib import SMTPException

def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()

def send_activation_key(user):

    print(user.__class__)
    activation_key = generate_activation_key(user.username)

    subject = "PathBuilder Account Verification"

    message = '''\n
                Please visit the following link to verify your account \n\n{0}://{1}/accounts/register/activate/?key={2}
                '''.format('https','pathbuilder.herokuapp.com', activation_key)            

    error = False

    try:
        send_mail(subject, message,'aemed.akef.1@gmail.com' , [user.email])
        user.author.activation_key = activation_key
        user.author.save()

    except SMTPException:
        error = True

   
    return not error
