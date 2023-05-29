#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ssl
import json
import ast
import requests


ssl._create_default_https_context = ssl._create_unverified_context
# In[2]:


auth_address = "https://dtmsintegrations.kwixee.co.in/api/Integration/GetToken"
base_address = "https://dtmsapi.kwixee.co.in/"


# In[3]:


def get_authtoken():
    # data={"grant_type":"client","Id":"dtmsadmin@gmail.com","SecretKey":"5b466ad0020d4b8","client_id":"Quixy"}
    data={"grant_type":"client","Id":"dtmsadmin@gmail.com","SecretKey":"b1829de2c86f4d1","client_id":"Quixy"}


    #a=requests.post(auth_address+"connect/token",data=data)
    a=requests.get(auth_address,data=data,verify=False)
    temp=a.content
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
gsfid_url = base_address+"api/Report/GetData?id=09112022-195342863-cd239dcc-f64c-4c3f-ae50-710521db1835"
print("Collecting GSFID Data from :", gsfid_url)
try:
    response = requests.post(gsfid_url, json=data, headers=headers, verify=False)
    xgsfid=response.json()["results"]
    # print(response)
    print(json.dumps(xgsfid, indent=4))
except Exception as e:
    print("error : ",e)
    xgsfid = "error collecting data from "+gsfid_url+", error :"+e


# In[9]:


#GATE DATA

gatedata_url = base_address+"api/Report/GetData?id=09112022-195343862-b7086592-2af9-4fdc-9362-8bfb85797f97"
print("Collecting GATE Data from :", gatedata_url)
try:
    response = requests.post(gatedata_url, json=data , headers=headers, verify=False)
    gate_data=response.json()["results"]
    print(len(gate_data))
    print(json.dumps(gate_data, indent=4))
except Exception as e:
    gate_data = ["error collecting data from "+gatedata_url+", error :"+str(e)]

# In[10]:


#terminal data


terminal_url = base_address+"api/Report/GetData?id=09112022-195345737-704c7870-4c68-407d-806f-2f6a2907cdc2"
try:
    print("Collecting Terminal Data from :", terminal_url)
    response = requests.post(terminal_url, json=data , headers=headers, verify=False)
    terminal_data=response.json()["results"]
    print(len(terminal_data))
    print(json.dumps(terminal_data, indent=4))
except Exception as e:
    terminal_data = ["error collecting data from "+terminal_url+", error :"+str(e)]
    

# In[11]:


# TRUCK DATA
truck_url = base_address + 'api/Report/GetData?id=09112022-195345404-7300b28b-dfc3-4089-81d3-bb457c2dee10'
try:
    print("Collecting Truck Data from :", truck_url)
    response = requests.post(truck_url, json=data , headers=headers, verify=False)
    truck_data=response.json()["results"]
    print(len(truck_data))
    print(json.dumps(truck_data, indent=4))
except Exception as e:
    truck_data = "error collecting data from "+truck_url+", error :"+str(e)


# In[12]:
#user data / security guard
user_server_url = base_address+"api/Report/GetData?id=09112022-195346186-46e384fc-e0e2-4010-a2b6-b0f963f3b42b"
try:
    print("Collecting user's Data from :", user_server_url)
    response = requests.post(user_server_url, json=data , headers=headers, verify=False)
    user_server_data=response.json()["results"]
    print(len(user_server_data))
    print(json.dumps(user_server_data, indent=4))
except Exception as e:
    user_server_data = "error collecting from "+user_server_url+", error :"+str(e)


# In[13]:


#DRIVER DATA for server


driver_server_url = base_address+"api/Report/GetData?id=09112022-195343189-cef7a637-747e-4d40-9b6e-89833f61bf51"
# try:
print("Collecting Driver Data from :", driver_server_url)    
response = requests.post(driver_server_url, json=data, headers=headers, verify=False)
driver_server_data=response.json()["results"]
print(json.dumps(driver_server_data, indent=4))
# except Exception as e:
#     driver_server_data = "error collecting from "+driver_server_url+", error :"+str(e)

# In[14]:


#TRANSACTION 

transaction_url = "https://dtmsapi.kwixee.co.in/api/ExternalApi/Save"
# transaction_url = base_address + "api/ExternalApi/Save"
# transaction_url = base_address+"api/ExternalApi/SaveAppData"

# transaction_url = "http://183.82.112.4:8050/api/ExternalApi/Save"
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


try:
    response = requests.post(transaction_url, json=t_data, headers=headers, verify=False)
    transaction_data=response.json()
    print(json.dumps(transaction_data, indent=4))
except Exception as e:
    print("error in transaction api :", e)
    transaction_data = "error in transaction api :"+str(e)


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
 "USER DATA URL" : user_server_url,
 "USER DATA RESPONSE OBJECT" : user_server_data,
 "DRIVER DATA URL" : driver_server_url,
 "DRIVER DATA RESPONSE OBJECT" : driver_server_data,
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
 "USER DATA URL" : user_server_url,
 "USER DATA RESPONSE OBJECT" : user_server_data[0],
 "DRIVER DATA URL" : driver_server_url,
 "DRIVER DATA RESPONSE OBJECT" : driver_server_data[0],
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