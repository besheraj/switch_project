import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import data_terminal
# Create your views here.

# Create your views here.
# one parameter named request
def csv_upload(request):
    # declaring template
    template = "data_terminal/upload_data.html"

    data = data_terminal.objects.all()

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = data_terminal.objects.update_or_create(
            SW=column[0],
            T1=column[1],
            T2=column[2],
            T3=column[3],
            T4=column[4],
            T5=column[5],
            TS=column[6]
        )
    context = {}

    return render(request, template, context)




def showdata(request):
    return render(request, showdata.html)
