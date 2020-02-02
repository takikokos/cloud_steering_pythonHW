#!/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Pass file with coordinates as a parameter")
    for fname in sys.argv[1:]:
        with open(fname, "r") as inp_file:
            for line in inp_file.readlines():
                latitude, longitude, *_ = line.rstrip().split(";")
                latitude = float(latitude.replace(",", ".").rstrip("'"))
                longitude = float(longitude.replace(",", ".").rstrip("'"))

                resp = requests.get(f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=geocodejson").json()
                query_coords = resp["geocoding"]["query"]
                location_desc = resp["features"][0]["properties"]["geocoding"]["label"]

                print(f"Input data : {line.rstrip()}")
                print("Output data :")
                print(f"Location : {location_desc}")
                print(f"Goggle Maps URL: https://www.google.com/maps/search/?api=1&query={latitude},{longitude}\n")