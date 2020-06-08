
import requests

r = requests.get("https://www.subhendubiswal.com")
print(r.status_code)
print(r.ok)
