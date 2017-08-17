from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings

from loginlogout.utils import * # import re


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        if username.find("@funai.gov.br") > 0:
            username = validate_user_funai(username, "@funai.local")

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse(settings.URL_AFTER_LOGIN))
            else:
                msg = _('Your account is not active, Please contact the system administrator')
                return redirect(reverse(settings.URL_AFTER_LOGIN))
                #return render(request,  reverse(settings.URL_AFTER_LOGIN), {'msg': msg})
        else:
            print('deu erro render')
            msg = _('Invalid username or password')
            return redirect(reverse(settings.URL_AFTER_LOGIN))
            #return render(request, reverse(settings.URL_AFTER_LOGIN), context={'msg': msg})
    else:
	#return render(request, reverse(settings.URL_AFTER_LOGIN))
        return redirect(reverse(settings.URL_AFTER_LOGIN))

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect(reverse(settings.URL_AFTER_LOGIN))
