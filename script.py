import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello,{}".format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("subhendu"))

r = requests.get("https://www.subhendubiswal.com")
print(r.status_code)
