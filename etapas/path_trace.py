import json
import requests
from tabulate import tabulate
from apic_em_functions import *

requests.packages.urllib3.disable_warnings()


def get_flowId(source, destination):
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }
    body_json = {
        "destIP": destination,
        "sourceIP": source
        }
    resp = requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    print("Status of /flow-analysis request: ", resp.status_code)
    flowAnalysisId = ""
    if resp.status_code != 202 and resp.status_code != 200:
        
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    else:
        response_json = resp.json()
        flowAnalysisId = response_json["response"]["flowAnalysisId"]
    return flowAnalysisId

def print_flow(flowId):
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis/"
    api_url += flowId
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "Accept": "application/json",
     "X-Auth-Token": ticket
    }
    body_json = {
        "flowAnalysisId": flowId
        }
    resp = requests.get(api_url,json.dumps(body_json), headers=headers,verify=False)
    response_json = resp.json()
    while response_json["response"]["request"]["status"] != "COMPLETED":
        resp = requests.get(api_url,json.dumps(body_json), headers=headers,verify=False)
        response_json = resp.json()
        if resp.status_code != 202 and resp.status_code != 200:
            raise Exception("Status code does not equal 200. Response text: " + resp.text)
    route = []
    for node in response_json["response"]["networkElementsInfo"]:
        route.append(node["ip"])
    print(route)


print("Hosts:")
print_hosts()
print("Network devices:")
print_devices()

valid_route = False
while not valid_route:
    s_ip = input("Choose the source IP from the lists above: ")
    d_ip = input("Choose the destination IP from the list before: ")
    flow_id = get_flowId(s_ip, d_ip)
    if flow_id == "":
        print("The route you entered is not valid, please enter the IPs again:")
    else:
        valid_route = True
    
print(f"The flow id is {flow_id}")
print_flow(flow_id)
    
