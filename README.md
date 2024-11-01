Generate outbound and inbound time between ORIGIN and DEST

**Install:**

1- [Install Python](https://realpython.com/installing-python/) (>3.11)

2- Get Google Maps key [here](https://developers.google.com/maps/third-party-platforms/wordpress/generate-api-key) (The API is not free and will [incur cost](https://mapsplatform.google.com/pricing/))

3- Clone the repo

```git
https://github.com/muhyousri/travel_time.git
cd travel_time
python -m venv .
source bin/activate
pip install -r requirments.txt
```

**Run:**

MAPS_KEY=`<KEY>` ORIGIN=`<ORIGIN>` DEST=`<DEST>` python main.py

Output will be a csv in the same directory with format

time_of_day; inbound_time ; outbound_time
