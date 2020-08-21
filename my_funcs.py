#!usr/bin/env python

# Exercise '2b'

import yaml

def read_yaml(password):
    with open("device.yml") as f:
        yaml_data=yaml.load(f)
        yaml_data['password']=password
    return(yaml_data)

def out_yaml(arp_list):
    print ("\n IP Address\t--->\tMAC Address")
    print ("-"*40)
    for arp_entry in arp_list:
        print (arp_entry['address']+"\t\t"+arp_entry['hwAddress'])


