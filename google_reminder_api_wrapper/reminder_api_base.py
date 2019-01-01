import requests
import json
from .api_credentials import ApiCredentials

API_URL = 'https://reminders-pa.clients6.google.com/v1internalOP/reminders/'


class ReminderApiBase:
    credentials = ApiCredentials()
    auth_cookie = {
        'HSID': credentials.HSID,
        'SSID': credentials.SSID,
        'APISID': credentials.APISID,
        'SAPISID': credentials.SAPISID,
        'SID': credentials.SID
    }
    auth_key = credentials.key
    sapisid_hash_authorization = credentials.authorization

    def __init__(self):
        self.headers = {
            'x-origin': 'https://calendar.google.com',
            'content-type': 'application/json',
            'cache-control': 'no-cache',
            'authorization': self.sapisid_hash_authorization,
            'key': self.auth_key,
            'cookie': ';'.join('{}={}'.format(k, v) for k, v in self.auth_cookie.items())
        }

    def request(self, command, payload, is_protobuf_payload=False):
        if is_protobuf_payload:
            self.headers['content-type'] = 'application/json+protobuf'

        if payload:
            payload = json.dumps(payload)

        res = requests.post(url=API_URL + command,
                            data=payload,
                            headers=self.headers)

        # TODO: Make this more elegant
        if is_protobuf_payload:
            self.headers['content-type'] = 'application/json'

        if res.status_code != 200:
            raise Exception(res.reason, res.text)
        return json.loads(res.text)
