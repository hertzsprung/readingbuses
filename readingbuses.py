#!/usr/bin/env python
from __future__ import print_function
import csv
from datetime import datetime
from collections import defaultdict
from collections import OrderedDict

averageSpeed = defaultdict(list)

with open('daily-trip-2016-12-01_2016-12-05.csv', 'rb') as tripsFile:
    trips = csv.DictReader(tripsFile, delimiter=',')
#    print("field", trips.fieldnames)

    for trip in trips:
        if len(trip) != 0:
            date = datetime.strptime(trip['\xef\xbb\xbfDate'], "%d/%m/%Y")

            averageSpeed[date].append(float(trip['AverageSpeed']))
            
#            print(date, trip['TotalDrivingTime'], trip['TotalDistanceTravelled'], trip['AverageSpeed'], trip['NumberOfTrips'])

averageSpeed = {k: sum(v)/len(v) for k, v in averageSpeed.iteritems() }
averageSpeed = OrderedDict(sorted(averageSpeed.items(), key=lambda e: e[0]))
print(averageSpeed)
    
