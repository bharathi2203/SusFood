
from json import tool
import folium
import webbrowser 
from OSMPythonTools.nominatim import Nominatim 
import ssl 
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
from bing_image_downloader import downloader
import os
import pandas as pd
import random




overpass = Overpass()

ssl._create_default_https_context = ssl._create_unverified_context

nominatim = Nominatim()
areaId = nominatim.query('University of Pennsylvania').areaId()
print (areaId)


query1 = overpassQueryBuilder(area=areaId, elementType=['node', 'way'], selector=['"amenity"~"restaurant"'])
query2 = overpassQueryBuilder(area=areaId, elementType=['node', 'way'], selector=['"amenity"~"fast_food"'])
query3 = overpassQueryBuilder(area=areaId, elementType=['node', 'way'], selector=['"amenity"~"cafe"'])
result1 = overpass.query(query1)
result2 = overpass.query(query2)
result3 = overpass.query(query3)
# print (result1.countElements())
# print (result2.countElements())
# print (result3.countElements())
# print (result.elements())
# for x in result2.elements():
#     print (x.tags())
#     print (x.lat())
#     print (x.lon())
#     break

myDB = []
for restaurants in result1.elements():
    name = restaurants.tags()["name"]
    if "opening_hours" in restaurants.tags():
        opening_hours = restaurants.tags()["opening_hours"]
    else:
        opening_hours= 'Mo-Su 09:00 - 18:00'
    if "cuisine" in restaurants.tags():
        cuisine = restaurants.tags()["cuisine"]
    else:
        cuisine = "fancy"
    query_string = f'{name} {cuisine} "food" restaurant'
    # downloader.download(query_string, limit=1,  output_dir='dataset', 
    #     adult_filter_off=False, force_replace=False, timeout=200)
    picture = f"~/Downloads/dataset/{query_string}/Image_1.jpg"
    myDB.append({"Name": name,
                "rLat": restaurants.lat(),
                "rLong": restaurants.lon(),
                "picture": picture, 
                "opening_hours": opening_hours})
for fastFood in result2.elements():
    name = fastFood.tags()["name"]
    if "opening_hours" in fastFood.tags():
        opening_hours = fastFood.tags()["opening_hours"]
    else:
        opening_hours= 'Mo-Su 09:00 - 18:00'
    query_string = f"{name} food"
    # downloader.download(query_string, limit=1,  output_dir='dataset2', 
    #     adult_filter_off=False, force_replace=False, timeout=200)
    picture = f"~/Downloads/dataset/{query_string}/Image_1.jpg"
    myDB.append({"Name": name,
                "rLat": fastFood.lat(),
                "rLong": fastFood.lon(),
                "picture": picture, 
                "opening_hours": opening_hours})
for cafe in result3.elements():
    name = cafe.tags()["name"]
    picture = None 
    if "opening_hours" in cafe.tags():
        opening_hours = cafe.tags()["opening_hours"]
    else:
        opening_hours= 'Mo-Su 09:00 - 18:00'
    query_string = f"{name} 'cafe'"
    # downloader.download(query_string, limit=1,  output_dir='dataset3', 
    #     adult_filter_off=False, force_replace=False, timeout=200)
    picture = f"~/Downloads/dataset/{query_string}/Image_1.jpg"
    myDB.append({"Name": name,
                "rLat": cafe.lat(),
                "rLong": cafe.lon(),
                "picture": picture, 
                "opening_hours": opening_hours})
# print (myDB)

df = pd.DataFrame.from_dict(myDB)
df.to_csv(r'RestDataBase2.csv', index = True, header = True)
# print (df)

# map = folium.Map(location= [39.952583, -75.165222], zoom_start = 15)
# EDIT BELOW 
class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
    
    def showMap(self):
        #Create the map
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)

        #Display the map
        restDB = pd.read_csv("RestDataBase.csv")
        restloc = restDB.loc[0]
        colours = ["green", "blue", "red", "pink", "purple", "cyan"]
        for _, x in restDB.iterrows():
            folium.Marker (
            location = [x['rLat'], x['rLong']], popup = x["Name"], 
            tooltip = x['Name'],
            # Fix colours
            icon = folium.Icon(color = random(colours)), 

            ).add_to(my_map)
        my_map.save("map.html")
        webbrowser.open("map.html")


#Define coordinates of where we want to center our map
coords = [39.9522, -75.1932]
map = Map(center = coords, zoom_start = 25)
map.showMap()