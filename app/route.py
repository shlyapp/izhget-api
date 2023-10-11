from typing import NamedTuple, List
import requests

from utils import get_current_date, get_current_hours, get_current_minutes, get_route_values

class Route(NamedTuple):
    tram: str
    name: str
    departure_time: str
    arrival_time: str


def get_routes(tram_id: int, station_id: int, destination_id: int) -> List[Route]:
    url = 'https://xn--c1aff6b0c.xn--p1ai/rasp/load_station.php'
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = {'route': tram_id,
            'stn': station_id,
            'dstn': destination_id,
            'dt': get_current_date(),
            'th_rasp': get_current_hours(),
            'tm_rasp': get_current_minutes(),
            'timeint': 30}
    response = requests.post(url, headers=headers, data=data)

    routes = list()
    values = get_route_values(response.text)
    for value in values:
        routes.append(Route(value[0], value[1], value[2], value[3]))

    return routes



