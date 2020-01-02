import pathlib
from typing import Optional, Union, List
from calendar import monthrange
import requests
import json
import csv
import socket


API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    if path is None:
        p = pathlib.Path.joinpath(_path, pathlib.Path("{}_{}_{:02d}".format(woeid, year, month)))
    else:
        p = pathlib.Path(path, pathlib.Path("{}_{}_{:02d}".format(woeid, year, month)))
    if not pathlib.Path.exists(p):
        p.mkdir(parents=True)

    max_day = monthrange(year, month)[1]
    file_paths = []
    for day in range(1, max_day+1):
        try:
            r = requests.get("{}location/{}/{}/{}/{}".format(API_URL, woeid, year, month, day), timeout=timeout)
        except socket.timeout:
            raise requests.exceptions.Timeout
        if r.status_code != 200:
            raise requests.exceptions.HTTPError
        try:
            results = json.loads(r.text)
        except Exception:
            raise RuntimeError
        if not results:
            break
        file_path = "{}/{}_{:02d}_{:02d}.csv".format(p, year, month, day)
        file_paths.append(file_path)
        with open(file_path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=list(results[0].keys()))
            writer.writeheader()
            for result in results:
                writer.writerow(result)

    return str(p), file_paths


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
