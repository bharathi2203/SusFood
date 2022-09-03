
import folium
import webbrowser 
from OSMPythonTools.nominatim import Nominatim 
import ssl 
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
overpass = Overpass()

ssl._create_default_https_context = ssl._create_unverified_context

nominatim = Nominatim()
areaId = nominatim.query('Philadelphia, United States').areaId()
print (areaId)

query = overpassQueryBuilder(area=areaId, elementType=['node', 'way'], selector=['"amenity"~"restaurant"'])
result = overpass.query(query)
print (result.countElements())
print (result.elements())
for x in result.elements():
    print (x.tags())


# m = folium.Map(location= [39.952583, -75.165222], zoom_start = 15)
# EDIT BELOW 
# class Map:
#     def __init__(self, center, zoom_start):
#         self.center = center
#         self.zoom_start = zoom_start
    
#     def showMap(self):
#         #Create the map
#         my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)

#         #Display the map
#         my_map.save("map.html")
#         webbrowser.open("map.html")


# #Define coordinates of where we want to center our map
# coords = [39.952583, -75.165222]
# map = Map(center = coords, zoom_start = 5)
# map.showMap()