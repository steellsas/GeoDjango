import folium

lat = 37
long = 8
geo_json = r"C:\my porfolio\GeoMapDjango\MyMap\media\gz_2010_us_040_00_500k.json"
lt_geo = r"C:\my porfolio\GeoMapDjango\MyMap\media\LTU.geojson"

# file1 = open(lt_geo, encoding="utf-8")

# file = open(lt_geo, encoding="utf-8")
m = folium.Map(location=[lat,long],
               tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
               attr='My Data Attribution',
               zoom_start=7)

folium.GeoJson(lt_geo, name="geojson").add_to(m)



m.save('test_idir.index.html')
