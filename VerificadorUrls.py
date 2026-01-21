from urllib.request import Request,urlopen
from urllib.error import HTTPError, URLError

urls=["https://www.google.com", 
      "https://github.com",
      "https://www.cloudflare.com",
      "https://developer.mozilla.org"]

for url in urls:
    try:
        req=Request(url,headers={"User-Agent": "Mozilla/5.0"})
        res=urlopen(req)
        codigo=res.status
        print(f"{url} codigo de estado Http: {codigo}")
    except HTTPError as e:
        print("Error HTTP:", e.code)
    except URLError as e:
        print("Error de conexión:", e.reason)