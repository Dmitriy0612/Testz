from django.shortcuts import render
from .models import Articles,Articles2,Articles3,Articles4


def index(request):

    name=Articles.objects.all()
    name1=Articles2.objects.all()
    name2=Articles4.objects.filter(id_teacher='4')



    return render(request, 'main/index.html',{'name':name,'name1':name1,'name2':name2})

