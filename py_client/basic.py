import requests


endpoint ="http://www.httpbin.org/anything"
endpoint ="http://127.0.0.1:8000"

data = requests.get(endpoint,params={"abc":123},json={"query":"Hello World"})
print(data.json())