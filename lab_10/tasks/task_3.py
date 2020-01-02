import filecmp
import pathlib
from typing import Union

import pandas as pd
import numpy as np
import glob


API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    all_files = glob.glob(path + "/*.csv")
    li = []

    for filename in all_files:
        frame = pd.read_csv(filename, index_col=None, header=0)
        li.append(frame)

    df = pd.concat(li, axis=0, ignore_index=True)
    df['DOB'] = pd.to_datetime(df['created']).dt.strftime('%Y-%m-%d')
    df = df.query('applicable_date == DOB')
    df['created'] = pd.to_datetime(df['created']).dt.strftime('%Y-%m-%dT%H:%M')
    df = df.sort_values(by='created')
    df = df.rename(columns={'the_temp': 'temp'})
    df = df[['created', 'min_temp', 'temp', 'max_temp', 'air_pressure', 'humidity', 'visibility',
            'wind_direction_compass', 'wind_direction', 'wind_speed']]
    df.to_csv("{}.csv".format(path), index=None, header=True)


if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
