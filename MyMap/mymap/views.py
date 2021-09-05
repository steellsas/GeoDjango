from django.shortcuts import render,redirect
import pandas as pd

import os
import folium
# rom folium import plugins
# import numpy as np
# Create your views here.


def map_view(request):

    shp_dir = os.path.join(os.getcwd(),'media','shp')

    # folium
    #Lithuanina cordinate
    lat = 55.1735998
    long = 23.8948016

    # folium
    l=  -16.22
    l2= -71.59
    m = folium.Map(location=[lat,long],zoom_start=7)



    print('test2')
    ## style
    style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
    style_rivers = {'color': 'blue'}

    ## adding to view

    geo_json = r"C:\my porfolio\GeoMapDjango\MyMap\media\gz_2010_us_040_00_500k.json"
    folium.GeoJson(geo_json, name="geojson").add_to(m)


    #
    # folium.GeoJson(os.path.join(shp_dir, 'basin.geojson'), name='basin', style_function=lambda x: style_basin).add_to(m)
    # # folium.GeoJson(os.path.join(shp_dir, 'rivers.geojson'), name='geojson').add_to(mm)
    # # geo_file = 'media/shp/counties.geojson'
    # # folium.GeoJson(geo_file).add_to(m)
    #
    # print(m)
    # # folium.LayerControl().add_to(m)
    # print('ok2')
    # ## exporting
    m = m._repr_html_()
    # print('ok3')
    context = {'my_map': m}
    # ## rendering
    print('test4')
    return render(request,'map.html',context)
    #
    # Ę atsitiktiniu  sudeneruotu tasku sukrupavimas pagal vietove
    # N = 100  # number of marker
    #
    # map_eu = folium.Map(location=[43, 3],
    #                     zoom_start=4)
    #
    # points = np.array([
    #     np.random.uniform(low=54, high=56, size=N),
    #     np.random.uniform(low=21, high=25, size=N)]).T
    #
    # plugins.MarkerCluster(points).add_to(map_eu)


    # folium.Marker(location=[55.9175, 21.06861],
    #               popup='Default  Klaipeda, miestas prie juros',
    #               tooltip='Click here to see Popup',
    #               icon=folium.Icon(color='red',icon='none')).add_to(map)
    #
    # folium.Marker(location=[55.71722, 21.1175],
    #               popup='<strong>Marker3</strong>',
    #               tooltip='<strong>Click here to see Popup</strong>').add_to(map)
    #
    # folium.Marker(location=[55.87583, 21.250831],
    #               popup='<h3 style="color:green;">Klaipeda</h3>',
    #               tooltip='<strong>Click here to see Popup</strong>',
    #               icon = folium.features.CustomIcon('media/boottles.png', icon_size=(50, 50))
    #               ).add_to(map)

    # real coordinates

    # # ===== mouse position
    # formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    #
    # plugins.MousePosition(
    #     position='topright',
    #     separator=' | ',
    #     empty_string='NaN',
    #     lng_first=True,
    #     num_digits=20,
    #     prefix='Coordinates:',
    #     lat_formatter=formatter,
    #     lng_formatter=formatter,
    # ).add_to(map)
    #


    # df = pd.read_json(r'C:\my porfolio\GeoMapDjango\MyMap\media\shp\counties.geojson')
    # df.to_csv(r'C:\my porfolio\GeoMapDjango\MyMap\media\New_Products.csv', index=None)
    #

