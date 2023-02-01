from requests import post
from json import loads


def share(ttl, secret, password=None):
    url = 'https://onetimesecret.com/api/v1/share'
    open_url = 'https://onetimesecret.com/secret/'

    data = {'secret': secret, 'ttl': ttl}

    if password:
        data.update({'passphrase': password})

    res = loads(post(url, data=data).text)

    if 'message' in res.keys():
        return 0

    open_url += res['secret_key']

    return open_url
