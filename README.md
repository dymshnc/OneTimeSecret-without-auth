# OneTimeSecret-without-auth
**Using the functionality of the OneTimeSecret (onetimesecret.com) service without registration and authorization.**
```python
>>> share(7200, 'secret', 'password')
'https://onetimesecret.com/secret/t05dvi526ia3g1lpatmuwp8z3qp1ulx'
```

You can use `share()` in your projects. The file *main.py* is an example.
```python
from ots_req import share

TTL = 7200  # Time to live
SECRET = 'your_secret'
PASSWORD = 'your_password'

print(share(TTL, SECRET, PASSWORD))
```