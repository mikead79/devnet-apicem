from apic_em_functions import *
import requests

requests.packages.urllib3.disable_warnings()

print("""
You can interact with a Cisco APIC-EM sandbox.
What would you like to do?
1. Get a ticket
2. See the list of hosts in the network
3. See the list of network devices in the network
4. Get information about the route between two hosts(or devices)
""")

while True:
    op = input("Choose an operation (by entering the corresponding number or 0 to exit): ")
    if op == '1':
        print(f"Your ticket is {get_ticket()}")
    elif op == '2':
        print_hosts()
    elif op == '3':
        print_devices()
    elif op == '4':
        print_hosts()
        print_devices()
        source = input("Choose a source IP from the list above: ")
        destination = input("Choose a destination IP from the list above: ")
        print_flow(source, destination)
    elif op == '0':
        break
    print()
