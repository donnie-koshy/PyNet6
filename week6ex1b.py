#!/usr/bin/env python

# Request using PYeAPI library

import pyeapi

from getpass import getpass


connection=pyeapi.client.connect(transport="https",host="arista3.lasthop.io",port='443',
username="pyclass",
password=getpass())



device=pyeapi.client.Node(connection)

arp_table=device.run_commands("show ip arp")

arp_table_extracted=arp_table[0]['ipV4Neighbors']
print("IP Address --> MAC Address")
print("-"*30)

for entry in arp_table_extracted:   
    print (entry['address']+"-->"+entry['hwAddress'])

