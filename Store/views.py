from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})


def support(request):
    return render(request,'page_1.html',{})