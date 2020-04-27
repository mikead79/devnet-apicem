import json
import requests
from tabulate import *
from apic_em_functions import *

requests.packages.urllib3.disable_warnings()


api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
ticket = get_ticket()
headers = {
 "content-type": "application/json",
 "X-Auth-Token": ticket
}
resp = requests.get(api_url,headers=headers,verify=False)
print("Status of /host request: ", resp.status_code)
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)
response_json = resp.json()
host_list = []
i = 0
for device in response_json["response"]:
    i += 1
    host = [i, device["hostType"], device["hostIp"]]
    host_list.append(host)
table_header = ["Number", "Type", "IP"]
print(tabulate(host_list, table_header))
