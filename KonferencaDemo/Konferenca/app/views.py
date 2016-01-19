from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from app.models import Session
from app.forms import SessionForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth. mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'index.html') 

@login_required
def submit_session(request):
    return render(request, 'app/submit_session.html')

# obvezno moras uvozit 
class SessionList(ListView):
    model = Session

class SessionDetails(DetailView):
    model = Session

class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm

class UpdateSession(LoginRequiredMixin, UpdateView):
    model = Session
    form_class = SessionForm

class SessionDelete( LoginRequiredMixin, DeleteView):
    model = Session
    success_url = reverse_lazy('sessions_list')
