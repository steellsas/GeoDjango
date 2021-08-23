from django.shortcuts import render,redirect

# Create your views here.


def map_view(request):
    context={}
    return render(request,'map.html',context)