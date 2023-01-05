from django.shortcuts import render
from django.http import HttpResponse
from . import templates

def home(request):
  return render(request,'home.html')


def ticket(request):
  return render(request,'ticket.html',
  {'name':request.POST['name'],
  "coach":request.POST['coach'],
  'seat_num':request.POST['seat-number'],
  'date':request.POST['date'],
  'time':request.POST['time'],
  'start_station':request.POST['start-station'],
  'end_station':request.POST['leaving-station']})