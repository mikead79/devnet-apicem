import json
import requests

requests.packages.urllib3.disable_warnings()

def get_ticket():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Xj3BDqbU"
    }

    resp = requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    print("Ticket request status: ", resp.status_code)

    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    
    return serviceTicket

def print_hosts():
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


def print_devices():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }
    resp = requests.get(api_url,headers=headers,verify=False)
    print("Status of /network-device request: ", resp.status_code)
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()
    devices_list = []
    i = 0
    for device in response_json["response"]:
        i += 1
        host = [i, device["type"], device["managementIpAddress"]]
        devices_list.append(host)
    table_header = ["Number", "Type", "IP"]
    print(tabulate(devices_list, table_header))

print("The ticket is:", get_ticket())
