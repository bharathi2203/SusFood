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

"""
compute the sustainability index for a 
"""
def compute_sus(restaurant):
    s = 0
    s += max(5, (100 - 10*restaurant["distance"])) * 0.4    # out of 40
    s += restaurant["organic"]      # out of 20
    s += restaurant["packaging"]    # out of 20
    s += restaurant["leftovers"]    # out of 20
    return int(s)


"""
"""
def sort_by_sus(arr, search):
    best = []
    d = dict()
    for restaurant in arr:
        s = compute_sus(restaurant)
        restaurant["sus_index"] = s
        if search.lower() in restaurant["Name"].lower():
            best.append((s, [restaurant]))
        elif s in d:
            (d[s]).append(restaurant)
        else:
            d[s] = [restaurant]
    
    l = d.items()
    l = list(l)
    l.sort(reverse = True)
    best.extend(l)
    return best

def get_distance(og_coords, dest_coords):
    if og_coords[0] == None or dest_coords[0] == None or og_coords[1] == None or dest_coords[1] == None:
        return 100
    return ((og_coords[0] - dest_coords[0])**2 + (og_coords[1] - dest_coords[1])**2)**0.5

def combine(arr):
    new = []
    for a, x in arr:
        new.extend(x)
    return new 

"""
use request info from user to query the api and get list of restaurants
"""
def get_search_results(search_req):
    search_req = "University Of Pennsylvania"    
    areaId = nominatim.query(search_req).areaId()
    print (areaId)
    coordso = (39.9522, -75.1932)
    qr_main = overpassQueryBuilder(area=areaId, elementType=['node'])
    qr_main = overpass.query(qr_main)
    m = qr_main.elements()[0]
    coords = (m.lat(), m.lon())
    print(coords) 

    query1 = overpassQueryBuilder(area=areaId, elementType=['node', 'way'], selector=['"amenity"~"restaurant"'])
    query2 = overpassQueryBuilder(area=areaId, elementType=['node', 'way'], selector=['"amenity"~"fast_food"'])
    query3 = overpassQueryBuilder(area=areaId, elementType=['node', 'way'], selector=['"amenity"~"cafe"'])
    result1 = overpass.query(query1)
    result2 = overpass.query(query2)
    result3 = overpass.query(query3)

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
            cuisine = "general"
        if "'" in name: 
            name.replace("'", "")
        query_string = name + cuisine + "food restaurant"
        # downloader.download(query_string, limit=1,  output_dir='dataset', 
        #     adult_filter_off=False, force_replace=False, timeout=200)
        picture = "'/Users/swatianshu/Downloads/dataset/" + query_string + "/Image_1.jpg'"
        myDB.append({"Name": name,
                    "rLat": restaurants.lat(),
                    "rLong": restaurants.lon(),
                    "picture": picture, 
                    "cuisine": cuisine,
                    "opening_hours": opening_hours,
                    "distance": get_distance(coords, (restaurants.lat(), restaurants.lon())),
                    "organic": random.randint(0, 20), 
                    "packaging": random.randint(0, 20), 
                    "leftovers": random.randint(0, 20)  })

    for fastFood in result2.elements():
        name = fastFood.tags()["name"]
        if "opening_hours" in fastFood.tags():
            opening_hours = fastFood.tags()["opening_hours"]
        else:
            opening_hours= 'Mo-Su 09:00 - 18:00'
        if "'" in name: 
            name.replace("'", "")
        query_string = name + "food"
        # downloader.download(query_string, limit=1,  output_dir='dataset2', 
        #     adult_filter_off=False, force_replace=False, timeout=200)
        picture = "'/Users/swatianshu/Downloads/dataset2/" + query_string + "/Image_1.jpg'"
        myDB.append({"Name": name,
                    "rLat": fastFood.lat(),
                    "rLong": fastFood.lon(),
                    "picture": picture, 
                    "cuisine": "fast_food",
                    "opening_hours": opening_hours,
                    "distance": get_distance(coords, (restaurants.lat(), restaurants.lon())),
                    "organic": random.randint(0, 10), 
                    "packaging": random.randint(0, 20), 
                    "leftovers": random.randint(0, 5) })

    for cafe in result3.elements():
        name = cafe.tags()["name"]
        picture = "'/Users/swatianshu/Downloads/dataset3/" + query_string + "/Image_1.jpg'" 
        if "opening_hours" in cafe.tags():
            opening_hours = cafe.tags()["opening_hours"]
        else:
            opening_hours= 'Mo-Su 09:00 - 18:00'
        if "'" in name: 
            name.replace("'", "")
        query_string = name + " cafe"
        # downloader.download(query_string, limit=1,  output_dir='dataset3', 
        #     adult_filter_off=False, force_replace=False, timeout=200)
        picture = "'/Users/swatianshu/Downloads/dataset3/" + query_string + "/Image_1.jpg'"
        myDB.append({"Name": name,
                    "rLat": cafe.lat(),
                    "rLong": cafe.lon(),
                    "picture": picture, 
                    "cuisine": "cafe",
                    "opening_hours": opening_hours,
                    "distance": get_distance(coords, (restaurants.lat(), restaurants.lon())),
                    "organic": random.randint(0, 20), 
                    "packaging": random.randint(0, 20), 
                    "leftovers": random.randint(0, 20)  })
    # print (myDB)
    # df = pd.DataFrame.from_dict(myDB)
    # df.to_csv(r'RestDataBase2.csv', index = True, header = True)
    
    # send message notification 
    sor = sort_by_sus(myDB, search_req)
    final = combine(sor)
    df = pd.DataFrame.from_dict(final)
    df.to_csv(r'sortedUPennDB.csv', index = True, header = True)
    return final

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
        restDB = pd.read_csv("RestDataBase2.csv")
        restloc = restDB.loc[0]
        colours = ["green", "blue", "red", "pink", "purple", "cyan"]
        for _, x in restDB.iterrows():
            url = x['picture']
            # print (url)
            folium.Marker (
            location = [x['rLat'], x['rLong']], 
            popup = "<h1 style = 'text-align:center; font-family:Gaegu'>" + x["Name"]+ "</h1>" + "<img src =" + f"{url}" + 
            "width = 300px, height = 300px>" + "<p> Opening hours: " + x["opening_hours"] + "</p>", 
            tooltip = x['Name'], icon = folium.Icon(icon = 'heart', icon_color = 'white', color =random.choice(colours))).add_to(my_map)
        my_map.save("map.html")
        webbrowser.open("map.html")

#Define coordinates of where we want to center our map
coords = (39.9522, -75.1932)

map = Map(center = coords, zoom_start = 25)
print("done")
map.showMap()

arr = get_search_results("University Of Pennsylvania")
for x in arr:
    print("\n", x, "\n")