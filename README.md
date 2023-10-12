<br />
<div align="center">
  <a href="https://github.com/shlyapp/izhget-python">
    <img src="images/logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">izhget-python</h3>

  <p align="center">
    simple api wrapper
    <br />
    <a href="https://github.com/shlyapp/izhget-python/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://ижгэт.рф/rasp/">Izhget site</a>
  </p>
</div>

## About The Project
This project is a simple wrapper over the [izhget](https://ижгэт.рф/rasp/) website API to get streetcar schedule data.

## Getting Started
To get a local copy up and running follow these simple example steps.

1. Clone the repo
  ```sh
  git clone https://github.com/shlyapp/izhget-python.git
  ```
2. Install requirements
  ```sh
  pip install -r requirements.txt
  ```
3. Done!

## Usage
A simple example of obtaining stop data for a streetcar:
``` python
from station import get_stations
from tram import get_trams


tram = get_trams()[0]
stations = get_stations(tram.id)

for count, station in enumerate(stations):
    print(f'Count: {count}\n' +
          f'Name: {station.name}\n' +
          f'Id: {station.id}\n')
```

_For more examples, please refer to the [Documentaion](https://github.com/shlyapp/izhget-python/wiki) or see [folder](https://github.com/shlyapp/izhget-python/tree/main/examples)_

## Roadmap
- [ ] upload on [PyPI](https://pypi.org/)

See the [open issues](https://github.com/shlyapp/izhget-python/issues) for a full list of proposed features (and known issues).

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact
Daniil - @shlyapp (telegram) or shlyapp.istu@gmail.com
