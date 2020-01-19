import pytest
import requests
import requests_mock

from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)

in_json = [{'title': 'Warsaw', 'location_type': 'City', 'woeid': 523920, 'latt_long': '52.235352,21.009390'},
     {'title': 'Newark', 'location_type': 'City', 'woeid': 2459269, 'latt_long': '40.731972,-74.174179'}]
out_json = {'Warsaw': 523920, 'Newark': 2459269}


@pytest.mark.parametrize(
    'url, city, json, status_code, expected',
    [
        pytest.param('/api/location/search?query=Warszawa', 'Warszawa', [], 200, {}),
        pytest.param('/api/location/search?query=War', 'War', in_json, 200, out_json),
    ],
)
def test_run_parametrize(url, city, json, status_code, expected):
    with requests_mock.Mocker() as m:
        m.get(url, json=json, status_code=status_code)
        assert get_cities_woeid(city) == expected


@pytest.mark.parametrize(
    'url, city, timeout, status_code',
    [
        pytest.param('/api/location/search?query=War', 'War', 0.1, 200),
    ],
)
def test_timeout(url, city, timeout, status_code):
    try:
        with requests_mock.Mocker() as m:
            m.get(url, exc=requests.exceptions.Timeout)
        get_cities_woeid(city, timeout)
    except Exception as exc:
        assert isinstance(exc, requests.exceptions.Timeout)
