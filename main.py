from ots_req import share

TTL = 7200  # Time to live
SECRET = 'your_secret'
PASSWORD = 'your_password'

print(share(TTL, SECRET, PASSWORD))
