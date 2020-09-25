import numpy as np
import pandas as pd
import pickle

data = pd.read_csv("Network_Traffic_Traces.csv")
mac = pd.read_csv("mac_address.csv")

mac_addresses = np.unique((data["mac.src"]))

mac_dict = {}
for k,i in enumerate(mac["Mac_Address"].values):
    mac_dict[mac["IoT_Devices"].values[k]] = i[-8:]
    
 
model = pickle.load(open('model.pkl', 'rb'))

def Predict(dns,port,pkt_size):
    index = model.predict([[dns, port, pkt_size]])
    for j,i in enumerate(mac_dict):
        if(j==index):
            return (i)

# print(Predict(4430,192,900))
# print(mac_dict)
