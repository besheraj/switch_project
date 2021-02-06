import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Data_Terminal
from datetime import datetime, timedelta
import json
# Create your views here.

# Create your views here.

# uploading the csv to datebase
def csv_upload(request):
    # declaring template
    template = "data_terminal/upload_data.html"

    data = Data_Terminal.objects.all()

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Data_Terminal.objects.update_or_create(
            SW=column[0],
            Status=column[1] or column[2] or column[3] or column[4] or column[5],
            TS=column[6]
        )
    context = {}

    return render(request, template, context)



# views to show the charts 
def charts(request):
    template = "data_terminal/charts.html"
    fromto = request.POST['fromto']
    dt_range = fromto.split(' to ')
    data = []
    if len(dt_range) > 0:
        from_ts = int(datetime.strptime(dt_range[0], '%Y-%m-%d %H:%M').strftime("%s"))
        to_ts = int(datetime.strptime(dt_range[1], '%Y-%m-%d %H:%M').strftime("%s"))
        
        data = Data_Terminal.objects.filter(SW='S1', TS__range=(from_ts, to_ts)).order_by('TS')
    else: 
        data = Data_Terminal.objects.filter(SW='S1').order_by('TS')
    sw1_data = []

    for sw in data:
        item: dict =  {'x': sw.TS*1000 , 'y': sw.Status}
        sw1_data.append(item)

    context = {
        'sw1_data':json.dumps(sw1_data),
        'fromto': fromto
    }
    return render(request, template, context)
