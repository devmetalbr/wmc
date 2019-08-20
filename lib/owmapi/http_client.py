import requests
import json


class HttpClient(object):
    """

    """
    @staticmethod
    def get_json(uri, params=None, headers=None):
        try:
            resp = requests.get(uri, params=params, headers=headers)
        except requests.exceptions.SSLError as e:
            raise Exception(str(e))
        except requests.exceptions.ConnectionError as e:
            raise Exception(str(e))
        except requests.exceptions.Timeout:
            raise Exception('API call timeouted')
        HttpClient.check_status_code(resp.status_code, resp.text)
        try:
            return resp.json()
        except:
            raise Exception('Impossible to parse API response data')


    @classmethod
    def check_status_code(cls, status_code, payload):
        if status_code < 400:
            return
        if status_code == 400:
            raise Exception(payload)
        elif status_code == 401:
            raise Exception(f'{status_code}: Invalid API Key provided')
        elif status_code == 404:
            raise Exception(f'{status_code}: Unable to find the resource')
        elif status_code == 502:
            raise Exception(f'{status_code}: Unable to contact the upstream server')
        else:
            raise Exception(payload)


if __name__ == '__main__':
    params = {'q': 'Ribeirão Preto', 'appid': 'fa1eda1795b99712e2058432d23e8e1e'}
    client = HttpClient()
    r = client.get_json('https://api.openweathermap.org/data/2.5/weather', params)
    print(r)