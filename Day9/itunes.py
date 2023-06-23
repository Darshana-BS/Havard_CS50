import json
import requests
import sys   #ability to use the command line 

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=weezer", sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["trackName"])
# print(json.dumps(response.json(), indent = 2))    

# https://reqres.in/api/users/2


# print(response.json())