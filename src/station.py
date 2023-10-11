from typing import NamedTuple, List
import requests 

from utils import get_values_from_tag, get_current_date


class Station(NamedTuple):
    name: str
    id: int


def get_stations(tram_id: int) -> List[Station]:
    url = 'https://xn--c1aff6b0c.xn--p1ai/rasp/list_station.php'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'route': tram_id, 
            'dt': get_current_date()}
    response = requests.post(url, headers=headers, data=data)

    values = get_values_from_tag(response.text, 'value')
    stations = list()
    for name, id in values.items():
        stations.append(Station(name, id))
    return stations[1:]


def get_destinations(tram_id: int, station_id: int) -> List[Station]:
    url = 'https://xn--c1aff6b0c.xn--p1ai/rasp/list_station.php'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'route': tram_id, 
            'dt': get_current_date(), 
            'stn': station_id}
    response = requests.post(url, headers=headers, data=data)

    values = get_values_from_tag(response.text, 'value')
    stations = list()
    for name, id in values.items():
        stations.append(Station(name, id))
    return stations[1:]

