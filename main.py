#!/usr/bin/env python3

from datetime import datetime
import os
import logging
import csv
import googlemaps


API_KEY = os.environ['MAPS_KEY']
HOME = os.environ['ORIGIN']
WORK = os.environ['DEST']
time_now = datetime.now().strftime('%A %H:%M')
today_date = datetime.today().date()
home_dir = os.getcwd()
gmaps = googlemaps.Client(key=API_KEY)
print(home_dir)


def convert_hhmm(seconds):
    """converts to HH:MM"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"


def get_times(origin, dest):
    """Gets times"""
    try:
        outbound_seconds = gmaps.directions(
            destination=dest, origin=origin, departure_time="now")[0]["legs"][0]["duration_in_traffic"]["value"]
    except (IndexError, KeyError) as e:
        print(f"Error getting outbound duration: {e}")
    try:
        return_seconds = gmaps.directions(
            destination=origin, origin=dest, departure_time="now")[0]["legs"][0]["duration_in_traffic"]["value"]
    except (IndexError, KeyError) as e:
        print(f"Error getting outbound duration: {e}")

    outbound_hours = convert_hhmm(outbound_seconds)
    return_hours = convert_hhmm(return_seconds)
    return outbound_hours, return_hours


with open(f"{home_dir}/report-{today_date}", 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    outbound_hours, return_hours = get_times(HOME, WORK)
    csv_writer.writerow(
        [time_now, outbound_hours, return_hours])
print("All done..")
