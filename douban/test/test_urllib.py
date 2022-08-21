from urllib.request import urlopen
import chardet
url_1 = "https://github.com/huoma/crawler"
url_2 = "https://www.douban.com" # 上来试试就418，teapot /ref:https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418
url_3 = "http://jandan.net/"
with urlopen(url_3) as response:
    html = response.read()
    print(chardet.detect(html))
    encoding = chardet.detect(html)["encoding"]

print(html.decode(encoding))
