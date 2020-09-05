#!usr\bin\env python

import pyeapi
import my_funcs

from getpass import getpass
from pprint import pprint

password=getpass()
device_dict=my_funcs.read_yaml(password)

connection=pyeapi.client.connect(**device_dict)

device=pyeapi.client.Node(connection)

output=device.enable("show ip route")

#pprint (output)

routes_dict=output[0]['result']['vrfs']['default']['routes']
#pprint(routes_dict)

for route,attribute in routes_dict.items():
	print ("\n"+route)
	if attribute['routeType']=='connected':
		print ("Route is Connected route")
	elif attribute['routeType']=='static':
		print ("Route is Static route")
		print ("Next hop address is "+attribute['vias'][0]['nexthopAddr']) 

