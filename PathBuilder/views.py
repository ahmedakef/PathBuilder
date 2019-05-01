from django.views import generic
from paths.forms import UserCreateForm
from paths.models import Author
from django.views import View
from django.conf import settings    
from django.core.mail import send_mail
from django.contrib import messages
from .helpers import send_activation_key
from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token


class Register(generic.CreateView):

    form_class = UserCreateForm
    template_name = 'forms.html'
    success_url='/paths'
    
    def form_valid(self,form):
        
        response = super().form_valid(form)
        # create author
        Author.objects.create(user=self.object)
        # generate and send activation key
        send_activation_key(self.object)
        Token.objects.create(user=self.object)
        # send email verification now
        success_message = 'Account created! Click on the link sent to your email to activate the account'
        messages.add_message(self.request, messages.INFO,success_message )

        return response


def ActivateAccount(request):
    key = request.GET.get('key',None)
    if not key:
        messages.warning(request, 'Please follow the link sent in the email.')
    else:
        try:
            author = Author.objects.get(activation_key=key, email_validated=False)
        except:
            author = None

        if author:
            author.user.is_active = True
            author.user.save()
            author.email_validated = True
            author.save()
        else:
            messages.warning(request, 'The activation key is not valid.')

    return render(request, 'registration/activated.html')

def send_activation_keyView(request):
    if send_activation_key(request.user):
        success_message = 'Click on the link sent to your email to activate the account'
        messages.add_message(request, messages.INFO,success_message )
    else:
        messages.add_message(request, messages.INFO, 'Unable to send email verification. Please try again')
    return redirect('paths:index')
