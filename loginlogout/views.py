from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings

from loginlogout.utils import * # import re


def login_view(request):
    context = RequestContext(request)
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
                return render_to_response(
                    'loginlogout/login_user.html',
                    {'msg': msg}, context_instance=context
                )
        else:
            msg = _('Invalid username or password')
            return render_to_response(
                'loginlogout/login_page.html',
                {'msg': msg}, context_instance=context
            )
    else:
        return render_to_response(
            'loginlogout/login_page.html',
            context_instance=context
        )


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect(reverse(settings.URL_AFTER_LOGIN))
