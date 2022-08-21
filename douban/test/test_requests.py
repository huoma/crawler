import requests
import chardet

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
headers = {"User-Agent": user_agent}
url = "https://www.google.com/"
r = requests.get(url, headers=headers)

for cookie in r.cookies.keys():
    print(cookie + ":" + r.cookies.get(cookie))

###
url2 = "https://www.liuxue86.com"
url3 = "http://jandan.net/"
url4 = "https://demo.eleadmin.com/login"
session = requests.session()
req = session.get(url4, allow_redirects=True)

params = {"admin": "xxx"}

req = session.post(url2, allow_redirects=True)

print(req.content.decode(chardet.detect(req.content)["encoding"]))

res = requests.get(url3)
print(res.content.decode("utf-8"))