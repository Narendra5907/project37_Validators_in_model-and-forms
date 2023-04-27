from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.
def insert_topic(request):
    TP=TopicForm()
    d={'TP':TP}
    if request.method=='POST':
        TD=TopicForm(request.POST)
        if TD.is_valid():
            TD.save()
            return HttpResponse('Topic is inserted')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_topic.html',d)



