import requests
import json
import socket


def get_cities_woeid(query: str, timeout: float = 5.):
    try:
        r = requests.get("https://www.metaweather.com/api/location/search/?query={}".format(query), timeout=timeout)
    except socket.timeout:
        raise requests.exceptions.Timeout
    if r.status_code != 200:
        raise requests.exceptions.HTTPError
    ret_dict = {}
    try:
        for result in json.loads(r.text):
            ret_dict[result['title']] = result['woeid']
    except Exception:
        raise RuntimeError

    return ret_dict


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
