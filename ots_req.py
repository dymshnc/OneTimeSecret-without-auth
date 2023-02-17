import requests


def share(ttl, secret, password=None):
    url = 'https://onetimesecret.com/api/v1/share'
    open_url = 'https://onetimesecret.com/secret/'

    data = {'secret': secret, 'ttl': ttl}

    if password:
        data['passphrase'] = password

    res = requests.post(url, data=data).json()

    if 'message' in res:
        return 0

    open_url += res['secret_key']

    return open_url
