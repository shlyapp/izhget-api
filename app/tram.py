from typing import NamedTuple, List
import requests

from utils import get_values_from_tag


class Tram(NamedTuple):
    name: str
    id: int


def get_trams() -> List[Tram]:
    response = requests.get("https://xn--c1aff6b0c.xn--p1ai/rasp/")
    values = get_values_from_tag(response.text, 'value')
    trams = list()
    for name, id in values.items():
        trams.append(Tram(name, id))
    return trams



    
