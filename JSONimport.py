import json
import requests
from requests.auth import HTTPBasicAuth
import csv
import pandas as pd

# src_json_node = '...d.dh/node/62'
el_pid = 4723109
# json_url = src_json_node + "/" + str(el_pid)
# print(json_url)

# authentication using rest un and pw
jfile = open("/var/www/python/auth.private")
jj = json.load(jfile)
src_json_node = jj["src_json_node"]
json_url = src_json_node + "/" + str(el_pid)

rest_uname = jj["auths"]["rest_uname"]
rest_pass = jj["auths"]["rest_pw"]
basic = HTTPBasicAuth(rest_uname, rest_pass)
print(basic)

print(json_url)
# Opening JSON file
jraw =  requests.get(json_url, auth=basic)
# model_json = jraw.content.decode('utf-8')
# print(model_json)


###############################################################
# response = requests.get(json_url)
# jraw = requests.get(json_url, auth=basic)
print(jraw)
###############################################################


# # model class reader
# def model_class_reader
#     # returns JSON object as 
#     # a dictionary
#     model_data = json.dump(model_json)
#     mlist = list(model_data)
#     # now extract the model using the name
#     model_data= model_data[mlist[0]]
#     for k in model_data.keys():
#         print(k)

# returns JSON object as 
# a dictionary
# model_data = json.loads(model_json)
# mlist = list(model_data)
# now extract the model using the name
# model_data= model_data[mlist[0]]
# for k in model_data.keys():
#     print(k)