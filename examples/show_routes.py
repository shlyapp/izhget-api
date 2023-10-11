from app.station import get_stations, get_destinations
from app.tram import get_trams
from app.route import get_routes


tram = get_trams()[2]
station = get_stations(tram.id)[21]
destination = get_destinations(tram.id, station.id)[0]
routes = get_routes(tram.id, station.id, destination.id)

for count, route in enumerate(routes):
    print(f'Count: {count}\n' +
          f'Name: {route.name}\n' +
          f'Tram: {route.tram}\n' +
          f'Departure time: {route.departure_time}\n' +
          f'Arrival time: {route.arrival_time}\n')


