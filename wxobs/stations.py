# -*- coding: utf-8 -*-
"""
Stations
--------

The class for getting all the stations and creating a SQLite db for storing
them using the NWS API.  The api is located at:
https://api.weather.gov and the full description and specification is at:

https://www.weather.gov/documentation/services-web-api#/default/get_stations__stationId__observations_latest
"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------


# ---- System
from collections import OrderedDict
from datetime import datetime
import json
from pprint import pformat
import sqlite3

# ---- External
from bs4 import BeautifulSoup
import requests

# ----------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------


def get_states():
    """Create a dictionary of state abbreviations and names."""
    states_site = "https://www.50states.com/abbreviations.htm"
    states_table = BeautifulSoup(
        requests.get(states_site).text,
        features="html.parser",
    ).table

    states = OrderedDict()
    for row in states_table.findChildren(['tr']):
        tmp_state = []
        for cell in row.findChildren('td'):
            tmp_state.append(cell.text)
        if tmp_state:
            states[tmp_state[1]] = tmp_state[0]

    return states

# ----------------------------------------------------------------------------
# Class:  Station
# ----------------------------------------------------------------------------


class Station:
    """Object for getting and storing information for a single station."""

    def __init__(self, station="KIAD"):
        self.raw_data = json.loads(requests.get(
            f"https://api.weather.gov/stations/{station}"
        ).text)

        self.name = self.raw_data['properties']['name']
        self.icao = self.raw_data['properties']['stationIdentifier']
        self.time_zone = self.raw_data['properties']['timeZone']
        self.elevation = self.raw_data['properties']['elevation']['value']
        self.elev_unit = \
            self.raw_data['properties']['elevation']['unitCode'].split(":")[-1]
        self.coords = self.raw_data['geometry']['coordinates']
        self.lat = self.raw_data['geometry']['coordinates'][1]
        self.lon = self.raw_data['geometry']['coordinates'][0]

    def __str__(self):
        data = [
            f"ICAO:  {self.icao}",
            f"Name:  {self.name}",
            f"Time Zone: {self.time_zone}",
            f"Elevation: {self.elevation} {self.elev_unit}",
            f"Coordinates: {self.lat} / {self.lon}"
        ]

        return pformat(data)
