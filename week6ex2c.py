import pyeapi
import yaml
import my_funcs
from getpass import getpass

password=getpass()
device_dict=my_funcs.read_yaml(password)

connection=pyeapi.client.connect(**device_dict)
device=pyeapi.client.Node(connection)
output=device.enable("show ip arp")
arp_list=output[0]['result']['ipV4Neighbors']

my_funcs.out_yaml(arp_list)

