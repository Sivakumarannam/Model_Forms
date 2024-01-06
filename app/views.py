from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is done ')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WTFO=WebpageForm()
    d={'WTFO':WTFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is done')
    return render(request,'insert_webpage.html',d)

def insert_access_records(request):
    ATFO=AccessRecordsForm()
    d={'ATFO':ATFO}
    if request.method=='POST':
        AFDO=AccessRecordsForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('insert_access_records is done')
    return render(request,'insert_access_records.html',d)