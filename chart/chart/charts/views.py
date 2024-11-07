from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
import datetime
import time
from chart.charts.models import ChartData





@login_required
def line_chart_view(request):
    data = ChartData.objects.all()
    x_data = [int(time.mktime(item.dateTime.timetuple())) * 1000 for item in data]
    y_data = [item.value for item in data]

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
    chartdata = {'x': x_data,
                 'name1': 'series 1', 'y1': y_data, 'Data': extra_serie1, 'kwargs1': {'color': '#a4c639'},
                 }

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H %M %S',
            'tag_script_js': True,
            'jquery_on_ready': True,
        }
    }
    return render(request,'charts/line_chart.html', data)
