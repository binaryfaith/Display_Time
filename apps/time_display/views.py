from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
}
  return render(request,'time_display/index.html', context)