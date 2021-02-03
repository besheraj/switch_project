from django.shortcuts import render

# Create your views here.
def showdata(request):
    return render(request, showdata.html)
