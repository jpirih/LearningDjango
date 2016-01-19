# Create your views here.

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from google.appengine.api import users


def home(request):
    uporabnik = users.get_current_user()
    if uporabnik:
        prijavljen = True
        logout_url = users.create_logout_url('/')
        params = {'prijavljen': prijavljen, 'logout_url': logout_url, 'uporabnik': uporabnik}
        return render_to_response('home.html', params)
    else:
        prijavljen = False
        login_url = users.create_login_url('/')
        params = {'prijavljen': prijavljen, 'login_url': login_url, 'uporabnik': uporabnik}
        return render_to_response('home.html', params)
