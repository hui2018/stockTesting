import http.client

conn = http.client.HTTPSConnection("morningstar1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "morningstar1.p.rapidapi.com",
    'x-rapidapi-key': "d54890ff34msh82b8e33167565a7p1e9232jsn0206c3837c0e",
    'accept': "string"
    }

conn.request("GET", "/convenient/fundamentals/yearly/restated?Mic=XNAS&Ticker=MSFT", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
