import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

# Open an external YAML file that hosts device information and convert to Python data structure
with open("device.yml") as f:
    device_dict=yaml.load(f)


password=getpass()
device_dict['password']=password

#Open a PyeAPI connection
connection=pyeapi.client.connect(**device_dict)

#Create an instance of Arista device
device=pyeapi.client.Node(connection)

output=device.enable("show ip arp")

arp_list=output[0]['result']['ipV4Neighbors']

print ("\n IP Address\t--->\tMAC Address")
print ("-"*40)
for arp_entry in arp_list:
    print (arp_entry['address']+"\t\t"+arp_entry['hwAddress'])

