#!/usr/bin/env python3

from datetime import datetime
import os
import pwd
# TODO: add proper logging
import csv
import googlemaps


API_KEY = os.environ['MAPS_KEY']
HOME = '53.1913182,-6.8135572'
WORK = '53.3306141,-6.2499912'
time_now = datetime.now().strftime('%H:%M')
today_date = datetime.today().date()
home_dir = pwd.getpwuid(os.getuid()).pw_dir
gmaps = googlemaps.Client(key=API_KEY)


def convert_hhmm(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"


def get_times(origin, dest):
    outbound_seconds = gmaps.directions(
        destination=dest, origin=origin)[0]["legs"][0]["duration"]["value"]
    return_seconds = gmaps.directions(
        destination=origin, origin=dest)[0]["legs"][0]["duration"]["value"]
    outbound_hours = convert_hhmm(outbound_seconds)
    return_hours = convert_hhmm(return_seconds)
    return outbound_hours, return_hours


# TODO: Handle error
with open(f"{home_dir}/report-{today_date}", 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    outbound_hours, return_hours = get_times(HOME, WORK)
    csv_writer.writerow(
        [time_now, outbound_hours, return_hours])
print("All done..")
