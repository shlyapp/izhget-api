from src.tram import get_trams


trams = get_trams()

for count, tram in enumerate(trams):
    print(f'Count: {count}\n' +
          f'Name: {tram.name}\n' +
          f'Id: {tram.id}\n')
