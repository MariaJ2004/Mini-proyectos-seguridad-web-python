import http.client

headersSecurity=["X-Frame-Options","X-Content-Type-Options","Strict-Transport-Security"]
dominio="example.com"
conn=http.client.HTTPConnection(dominio)

conn.request("GET","/")
response=conn.getresponse()
headers=response.getheaders()
for header in headersSecurity:
    if header in headers:
        print(f"{header} presente")
    else:
        print(f"{header} no se encuentra presente")
        if header=="X-Frame-Options":
            print("Riesgo de clickjacking\n")
        elif header=="X-Content-Type-Options":
            print("Riesgo de interpretación incorrecta de archivos\n")
        else:
            print("El navegador podría aceptar HTTP inseguro\n")

