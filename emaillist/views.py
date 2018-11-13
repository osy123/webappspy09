from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist import models
from emaillist.models import Emaillist


def index(request):
   #results = models.fetchall()
   results = Emaillist.objects.all().order_by('-id')
   data = {'emaillist_list': results}
   return render(request, "emaillist/index.html",data)

def form(request):
    return render(request, 'emaillist/form.html')

def delete(request):
    password = request.POST['password']
    no = request.POST['no']

    models.delete((password,no))
    return HttpResponseRedirect("/guestbook")

def add(request):
    emaillist = Emaillist()

    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    return HttpResponseRedirect("/emaillist")