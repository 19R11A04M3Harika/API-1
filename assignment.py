import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://12095.atlassian.net/rest/api/3/myself"

auth = HTTPBasicAuth("harikapenumatsa942@gmail.com", "ATATT3xFfGF0K9LoQz6aHfN2PXm1th0GFNbWOrojQ4XZgJUiz8ts7RhwUnkH_IOmkClNULOpyaIW4oT4BA00XVYT4skEDiNNuSLxR1i3EosxBljJ-CiCBIKRAJ56K3dZ64MsZxo1BHyys9yEF_sWQImQ0ywRJsI7tvy5HvezZq9Nd4X5llD-M9I=4A58FABC")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))