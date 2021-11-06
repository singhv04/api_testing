#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import ast
import requests
from requests.structures import CaseInsensitiveDict


# In[2]:


auth_address = "http://10.67.178.71:8090/"
#auth_address = "http://dtmsids.kwixee.co.in/"
base_address = "http://10.67.178.71:8080/"
#base_address = "http://dtmsapi.kwixee.co.in/"


# In[3]:


def get_authtoken():
    data={"grant_type":"client","Id":"dtmsadmin@gmail.com","SecretKey":"5b466ad0020d4b8","client_id":"Quixy"}
    #a=requests.post("http://192.168.0.173:8060/connect/token",data=data)
    #a=requests.post("http://183.82.112.4:8060/connect/token",data=data)
    print("Collecting token from : ",auth_address+"connect/token")
    a=requests.post(auth_address+"connect/token",data=data)
    #https://ids.quixy.com/connect/token
    temp=a.content
    print(temp)
    y=ast.literal_eval(temp.decode('utf-8'))
    auth_token=y['access_token']
    data={"token": auth_token}
    with open('authtoken.txt', 'w') as outfile:
        json.dump(data, outfile)
    return [auth_address+"connect/token", auth_token]


# In[4]:


a = get_authtoken()
token_url = a[0]
auth_token = a[1]


# In[5]:


headers = {'Authorization': 'Bearer ' + auth_token, 'Content-type': 'application/json'}
data =  {
"ElementType": ""
,"DefaultValue": "Thu Oct 01 2020 00:00:00 GMT+0530 (India Standard Time)"
,"Type": "valueType"
,"LabelName": "UpdatedOn"
,"Condition": "Greater Than"
,"MappingType": "Static"
                  }    


# In[6]:


headers


# In[7]:


data


# In[8]:


#GSFID
gsfid_url = base_address+"api/Report/GetData?id=06012021-114318836-f8268005-47bf-437b-8010-51169bf3a594"
print("Collecting GSFID Data from :", gsfid_url)    
response = requests.post(gsfid_url, json=data, headers=headers)
xgsfid=response.json()
print(json.dumps(xgsfid, indent=4))


# In[9]:


#GATE DATA
gatedata_url = base_address+"api/Report/GetData?id=12102021-005411331-cdda5982-4cc1-4559-91d3-e562f43094e7"
print("Collecting GATE Data from :", gatedata_url)
response = requests.post(gatedata_url, json=data , headers=headers)
gate_data=response.json()
print(len(gate_data))
print(json.dumps(gate_data, indent=4))


# In[10]:


#terminal data
terminal_url = base_address+"api/Report/GetData?id=29092020-114411262-09744950-832a-4e6d-ab3e-aa63d27ccb5b"
print("Collecting Terminal Data from :", terminal_url)
response = requests.post(terminal_url, json=data , headers=headers)
terminal_data=response.json()
print(len(terminal_data))
print(json.dumps(terminal_data, indent=4))


# In[11]:


# TRUCK DATA
truck_url = base_address + 'api/Report/GetData?id=08062021-220946933-c3bc6222-f0fd-48f8-bc43-9cccf2d14a3f'
print("Collecting Truck Data from :", truck_url)
response = requests.post(truck_url, json=data , headers=headers)
truck_data=response.json()
print(len(truck_data))
print(json.dumps(truck_data, indent=4))


# In[12]:


#user data / security guard
user_url = base_address+"api/Report/GetData?id=01102020-105849828-d5f6f1bc-3b5f-4275-8100-b6bf569129ea"
print("Collecting user's Data from :", user_url)
response = requests.post(user_url, json=data , headers=headers)
user_data=response.json()
print(len(user_data))
print(json.dumps(user_data, indent=4))


# In[13]:


# DRIVER DATA

driver_url = base_address+"api/Report/GetData?id=25082020-182558254-76607655-f2c0-4aef-b166-83a2dcd489c9"
print("Collecting Driver Data from :", driver_url)    
response = requests.post(driver_url, json=data, headers=headers)
driver_data=response.json()
print(json.dumps(driver_data, indent=4))


# In[14]:


#TRANSACTION 


transaction_url = base_address+"api/ExternalApi/SaveAppData"
print("Collecting transaction respons Data from :", transaction_url)    
t_data = {
    "TerminalID": "string",
    "GateID": "string",
    "UserID": "string",
    "TruckID": "string",
    "TruckLicenseFound": "string",
    "TruckLicenseExpired": "string",
    "DriverID": "string",
    "DriverLicenseFound": "string",
    "DriverLicenseExpired": "string",
    "CommonCompanyID": "string",
    "FaceMatch": "string",
    "TransactionStatus": "string",
    "PINVerification": "string",
    "StageofFailure": "string",
    "ReasonofFailure": "string",
    "TimeStamp": "yyyy/MM/dd hh:mm a",
    "GatePreference": "string",
    "_AppId":"30092021-130840431-1beecb8c-75fd-47f5-8296-e24943c37115",
    "_UserEmailId":"dtmsadmin@gmail.com"
}

response = requests.post(transaction_url, json=t_data, headers=headers)
transaction_data=response.json()
print(json.dumps(transaction_data, indent=4))


# In[15]:


#auth_address


# In[16]:


summary = {"ACCESS TOKEN BASE URL" : auth_address,
 "API DATA BASE URL" :  base_address,
 "TOKEN URL" : token_url,
 "AUTH TOKEN" : auth_token,
 "HEADERS" : headers,
 "DATA" : data,
 "GSFID URL" : gsfid_url,
 "GSFID RESPONSE OBJECT" : xgsfid,
 "GATE DATA URL" : gatedata_url,
 "GATE DATA RESPONSE OBJECT" : gate_data,
 "TERMINAL URL" : terminal_url,
 "TERMINAL DATA RESPONSE OBJECT" : terminal_data,
 "TRUCK DATA URL" : truck_url,
 "TRUCK DATA RESPONSE OBJECT" : truck_data,
 "USER DATA URL" : user_url,
 "USER DATA RESPONSE OBJECT" : user_data,
 "DRIVER DATA URL" : driver_url,
 "DRIVER DATA RESPONSE OBJECT" : driver_data,
 "TRANSACTION URL" : transaction_url,
 "TRANSACTION API BODY" : t_data,
 "TRANSACTION DATA RESPONSE OBJECT" : transaction_data}


# In[17]:


#summary


# In[18]:


brief_summary = {"ACCESS TOKEN BASE URL" : auth_address,
 "API DATA BASE URL" :  base_address,
 "TOKEN URL" : token_url,
 "AUTH TOKEN" : auth_token,
 "HEADERS" : headers,
 "DATA" : data,
 "GSFID URL" : gsfid_url,
 "GSFID RESPONSE OBJECT" : xgsfid[0],
 "GATE DATA URL" : gatedata_url,
 "GATE DATA RESPONSE OBJECT" : gate_data[0],
 "TERMINAL URL" : terminal_url,
 "TERMINAL DATA RESPONSE OBJECT" : terminal_data[0],
 "TRUCK DATA URL" : truck_url,
 "TRUCK DATA RESPONSE OBJECT" : truck_data[0],
 "USER DATA URL" : user_url,
 "USER DATA RESPONSE OBJECT" : user_data[0],
 "DRIVER DATA URL" : driver_url,
 "DRIVER DATA RESPONSE OBJECT" : driver_data[0],
 "TRANSACTION URL" : transaction_url,
 "TRANSACTION API BODY" : t_data,
 "TRANSACTION DATA RESPONSE OBJECT" : transaction_data}


# In[19]:


#brief_summary


# In[20]:


with open("brief_summary.json", "w") as outfile:
    json.dump(brief_summary, outfile, indent=4)


# In[21]:


with open("summary.json", "w") as outfile:
    json.dump(summary, outfile, indent=4)

