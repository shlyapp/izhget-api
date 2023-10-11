from src.station import get_stations, get_destinations
from src.tram import get_trams


tram = get_trams()[2]
station = get_stations(tram.id)[21]
destinations = get_destinations(tram.id, station.id)

for count, destination in enumerate(destinations):
    print(f'Count: {count}\n' +
          f'Name: {destination.name}\n' +
          f'Id: {destination.id}\n')
