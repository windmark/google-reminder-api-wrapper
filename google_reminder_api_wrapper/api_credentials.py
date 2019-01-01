import os


class ApiCredentials:
    SID = os.environ.get('SID')
    HSID = os.environ.get('HSID')
    SSID = os.environ.get('SSID')
    APISID = os.environ.get('APISID')
    SAPISID = os.environ.get('SAPISID')

    key = os.environ.get('key')
    authorization = os.environ.get('authorization')
