"""
Module containing the PyOWM library main entry point
"""

from lib.owmapi.http_client import HttpClient
ROOT_API_URL = 'http://api.openweathermap.org/data/2.5'
FORECAST_URL = ROOT_API_URL + '/forecast/daily'


class OWM(object):
    """
    OWM subclass providing methods for each OWM Weather API 2.5 endpoint and ad-hoc API clients for the other
    OWM web APis. The class is instantiated with *jsonparser* subclasses, each one parsing the response
    payload of a specific API endpoint
    """
    def __init__(self, appid=None, language="en"):

        if appid is not None:
            assert isinstance(appid, str), "Value must be a string"
        self._APPID = appid
        self._language = language

    #  --- ENDPOINTS ---
    def forecast_at_place(self, name, cnt=7):
        """
        Queries the OWM Weather API for the currently observed weather at the
        specified toponym (eg: "London,uk")
        """

        assert isinstance(name, str), "Value must be a string"
        params = {
            'q': name,
            'lang': self._language,
            'cnt': cnt,
            'units': 'metric',
            'appid': self._APPID
        }

        client = HttpClient()
        json_data = client.get_json(FORECAST_URL, params=params, headers=None)
        return json_data


if __name__ == '__main__':
    from datetime import datetime
    ap = OWM(appid='c0c4a4b4047b97ebc5948ac9c48c0559', language='pt')
    r = ap.forecast_at_place('Ribeirão Preto')
    for l in r['list']:
        print(datetime.fromtimestamp(l['dt']), l)
