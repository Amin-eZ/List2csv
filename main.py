from functions import list2csv

# The following dictionaries are provided as examples, you can replace them by your own
D1 = {"Location": "US", "Company": "Texas Instruments", 1: "No", "State": "Texas", "City": "Dallas"}
D2 = {"School": "ESIX Caen", "City": "Caen", "Region": "Normandie", "Department": 14, "Location": "FR", 1: "Yes"}
D3 = {"Department": 38, "City": "Grenoble", "Region": "Auvergne-Rhone-Alpes", 1: "No", "Location": "FR", "Company": "STMicroelectronics"}
D4 = {"State": "California", "University": "University of California", 1: "Yes", "City": "Los Angeles", "Location": "US"}

# List that regroups the dictionaries

L = list()
Lis = list()
L.append(D1)
L.append(D2)
L.append(D3)
L.append(D4)
# Here, you can add your additional dictionaries using "append" method


list2csv(L)
