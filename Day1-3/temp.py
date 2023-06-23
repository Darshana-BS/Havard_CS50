import urllib3
resp = urllib3.request("GET", "https://httpbin.org/robots.txt")
resp.status
resp.data