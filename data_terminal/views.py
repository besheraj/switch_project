import csv, io
from django.forms.fields import MultiValueField
from django.shortcuts import render
from django.contrib import messages
from .models import Data_Terminal
from datetime import datetime 
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
            Status= '1' in (column[1] , column[2] , column[3] , column[4] , column[5]),
            TS=column[6]
        )
    context = {}

    return render(request, template, context)



# views to show the charts 
def charts(request):
    template = "data_terminal/charts.html"
    s1_data = []
    s2_data = []
    s3_data = []
    fromto = '2019-11-29 00:00 to 2019-11-30 23:59' # available test data
    if request.method == 'POST':
        fromto = request.POST['fromto']
        dt_range = fromto.split(' to ')
        from_ts = int(datetime.strptime(dt_range[0], '%Y-%m-%d %H:%M').strftime("%s"))
        to_ts = int(datetime.strptime(dt_range[1], '%Y-%m-%d %H:%M').strftime("%s"))       
        s1_data = Data_Terminal.objects.filter(SW='S1', TS__range=(from_ts, to_ts)).order_by('TS')
        s2_data = Data_Terminal.objects.filter(SW='S2', TS__range=(from_ts, to_ts)).order_by('TS')
        s3_data = Data_Terminal.objects.filter(SW='S3', TS__range=(from_ts, to_ts)).order_by('TS')
        
    else: 
        s1_data = Data_Terminal.objects.filter(SW='S1').order_by('TS')
        s2_data = Data_Terminal.objects.filter(SW='S2').order_by('TS')
        s3_data = Data_Terminal.objects.filter(SW='S3').order_by('TS')

    sw1_data = []
    sw2_data = []
    sw3_data = []

    for sw in s1_data:
        item: dict =  {'x': sw.TS*1000 , 'y': sw.Status}
        sw1_data.append(item)
    

    for sw in s2_data:
        item: dict =  {'x': sw.TS*1000 , 'y': sw.Status}
        sw2_data.append(item)
    

    for sw in s3_data:
        item: dict =  {'x': sw.TS*1000 , 'y': sw.Status}
        sw3_data.append(item)
    

    context = {
        'sw1_data':json.dumps(sw1_data),
        'sw2_data':json.dumps(sw2_data),
        'sw3_data':json.dumps(sw3_data),
        'fromto':fromto

    }
    return render(request, template, context)

def alertreport(request):
    tepmlate = "data_terminal/alertreport.html"
    ping_lost_data = Data_Terminal.objects.filter(Status=0).order_by('TS')
    no =0
    alertreport = []
    for lost in ping_lost_data:
        no += 1
        report: dict= {'PK': no ,'SW': lost.SW , 'Ping_Status': 'Ping Lost', 'TS': datetime.fromtimestamp(float(lost.TS)) }
        alertreport.append(report)


    context = {
        'alertreport' : alertreport
    }
    return render(request,tepmlate, context)