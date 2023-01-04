from django.shortcuts import render
from django.http import HttpResponse
from . import templates

def home(request):
  return render(request,'home.html')


def ticket(request):
  return render(request,'ticket.html',
  {'name':request.POST['name'],
  'seat_num':request.POST['seat-number'],
  'date':request.POST['date']})