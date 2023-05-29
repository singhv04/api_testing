
import ssl
import json
import ast
import requests




ssl._create_default_https_context = ssl._create_unverified_context


auth_address = "https://dtmsintegrations.kwixee.co.in/api/Integration/GetToken"
base_address = "https://dtmsapi.kwixee.co.in/"


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


driver_server_url = base_address+"api/Report/GetData?id=09112022-195343189-cef7a637-747e-4d40-9b6e-89833f61bf51"
# try:
print("Collecting Driver Data from :", driver_server_url)    
response = requests.post(driver_server_url, json=data, headers=headers)
driver_server_data=response.json()
print(json.dumps(driver_server_data, indent=4))