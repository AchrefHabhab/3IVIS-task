# charts/migrations/0002_insert_chart_data.py

from django.db import migrations
import time
import random
import datetime

def insert_chart_data(apps, schema_editor):
    ChartData = apps.get_model('charts', 'ChartData')

    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

    nb_element = 350
    xdata = range(nb_element)
    xdata = [start_time + x * 1000000000 for x in xdata]  # Adding 1000000 seconds for each element
    #print("Generated xdata:", list(xdata))
    xdata = [datetime.datetime.fromtimestamp(x / 1000) for x in xdata]  # Convert to seconds by dividing by 1000
    #print("Converted xdata to datetime:", xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    chart_data = [
        {
            "dateTime" : xdata[i],
            "value" : ydata[i]
        }
        for i in range(nb_element)
    ]
    for data in chart_data:
        ChartData.objects.create(dateTime=data['dateTime'], value=data['value'])

class Migration(migrations.Migration):
    dependencies = [
        ('charts', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(insert_chart_data),
    ]
