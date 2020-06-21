# Program using low level python "requests" library

import requests
import json

from pprint import pprint
from getpass import getpass

from urllib3.exceptions import InsecureRequestWarning

#Create variables for HTTP Request
http_headers={"Content-Type":"application/json-rpc;"}
username="pyclass"
password=getpass()
host="arista3.lasthop.io"
port="443"
url="https://{}:{}/command-api".format(host,port) #Compose URL

json_payload={
"jsonrpc" :"2.0",
"method":"runCmds",
"params":{
    "version":1,
    "cmds": ["show ip arp"],
    "format":"json"
},
"id":"1"
}
#Convert from Python data to JSON string
json_data=json.dumps(json_payload)

http_headers['Content-length']=str(len(json_data))

response=requests.post(url,headers=http_headers,auth=(username,password),data=json_data,verify=False)

#Extract the JSON data from the payload
response=response.json()

#Print JSON response
pprint(response)

#Extract the ARP Table (list) from the nested python data structure
arp_table = response['result'][0]['ipV4Neighbors']

print ("\n IP Address -> MAC Address")
print("-"*30)
for entry in arp_table:
	print (entry['address']+" -> "+entry['hwAddress'])


