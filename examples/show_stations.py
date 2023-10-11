from src.station import get_stations
from src.tram import get_trams


tram = get_trams()[2]
stations = get_stations(tram.id)

for count, station in enumerate(stations):
    print(f'Count: {count}\n' +
          f'Name: {station.name}\n' +
          f'Id: {station.id}\n')
