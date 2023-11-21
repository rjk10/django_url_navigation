from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def sachin(request):
    return render(request,'sachin.html')

def rohit(request):
    return render(request,'rohit.html')