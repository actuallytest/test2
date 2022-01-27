import streamlit as st
import pandas as pd
import numpy as np
import requests
import json


root = "https://intense-beach-04157.herokuapp.com/"
smartlocks_url = root + 'smartLocks/'
routers = root + 'routers/'
ics = root + "ics/"
web = root + "web/"

st.title('Default Passwords')


lock_models = ["Perkotek","ERD-1120","Efes Digital Panel","Mas","AC 13PX","Burg Wachter","DIP40","Lorex LR-DPH2","M100","MB05-03","MB DYF40","MLŞ 14-70","MLŞ 14-107","MRA 101","Netalsan Obsidian","ONDRIVE ED07","OP705","OP M400","OP M500","Pratik Kart","Desi Steely","Audio","Teknoline","Teknoline IMR18","Desi UTOPIC","WL02","D45","A20 Kapı Kilidi", "Kwikset 275 Contemporary Deadbolt"]

routers_models = []

ics_models = ["Schneider M340 FTP", "Schneider M340 Web", "Schneider Premium FTP", "Schneider Premium Web", "Siemens S7-1200", "GarrettCom Magnum Switch"]

web_techs = []

resp = requests.get(routers)
y = json.loads(resp.text)
#print(y[0]["brand"])
for i in range(len(y)):
     routers_models.append(y[i]["brand"] + " " + y[i]["model"])

resp = requests.get(web)
y = json.loads(resp.text)
#print(y[0]["brand"])
for i in range(len(y)):
     web_techs.append(y[i]["product"])

option = st.sidebar.selectbox('Select view', ('Router', 'Lock', 'Industrial Control Systems', 'Web'))

if option == "Router":
     st.title('Default Router Passwords')
     option2 = st.selectbox('Select your Router Model',routers_models)
     st.write('You selected:', option)
     i = routers_models.index(option2)
     i += 1
     resp = requests.get(routers + str(i))
     data = resp.json()
     st.write(data)

elif option == "Lock":
     st.title('Smart Locks in Turkey')
     option = st.selectbox('Select your Lock Model',lock_models)
     i = lock_models.index(option)
     i += 1
     #st.write(smartlocks_url + str(i))
     resp = requests.get(smartlocks_url + str(i))
     data = resp.json()
     st.write(data)

elif option == "Industrial Control Systems":
     st.title('ICS Passwords')
     option = st.selectbox('Select your ICS Model',ics_models)
     i = ics_models.index(option)
     i += 1
     #st.write(smartlocks_url + str(i))
     resp = requests.get(ics + str(i))
     data = resp.json()
     st.write(data)

elif option == "Web":
     st.title('Web Passwords')
     option = st.selectbox('Select your Web Technology',web_techs)
     i = web_techs.index(option)
     i += 1
     #st.write(smartlocks_url + str(i))
     resp = requests.get(web + str(i))
     data = resp.json()
     st.write(data)

st.write("Blog Post : https://sockpuppets.medium.com/bypassing-door-passwords-4004b8d7995")
st.write("Source Code : https://github.com/aydinnyunus/gateCracker")
st.write("https://github.com/aydinnyunus/gateCracker-REST")
