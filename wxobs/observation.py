# -*- coding: utf-8 -*-
"""
Observation
-----------

The class for getting and parsing a single observation from the NOAA/NWS
weather API.

The api is located at:  https://api.weather.gov and the full description and
specification is at:

https://www.weather.gov/documentation/services-web-api#/default/get_stations__stationId__observations_latest
"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------


# ---- System
from datetime import datetime
import json

# ---- External
import requests

# ----------------------------------------------------------------------------
# Class:  MetarOb
# ----------------------------------------------------------------------------


class Observation:
    """A single observation, it's associated properties and functionality."""

    def __init__(self, station="KIAD", ob_time=None):
        """Define the initial state of an observation."""
        if ob_time is None:
            ob_time = "latest"

        self.ob_time = ob_time
        self.station = station
        self.ob = self.get_ob()

    def get_ob(self, station=None, ob_time=None):
        if station is None:
            station = self.station
        if ob_time is None:
            ob_time = self.ob_time

        return requests.get(
            f"https://api.weather.gov/stations/{station}/observations/{ob_time}"
        ).json()

    @property
    def raw(self):
        return self.ob['properties']['rawMessage']
