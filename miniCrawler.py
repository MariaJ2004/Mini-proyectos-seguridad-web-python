from urllib.request import Request,urlopen
req=Request("https://httpbin.org/",headers={"User-Agent": "Mozilla/5.0"})
res=urlopen(req)
body=res.read().decode()

urls=[]

for links in body.split('href="'):
    print(links)
    if '"' in links:

        link=links.split('"')[0]
        urls.append(link)

print("Links encontrados: ")
for url in urls:
    print(url)