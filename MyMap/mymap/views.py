from django.shortcuts import render,redirect

import os
import folium
# Create your views here.


def map_view(request):

    shp_dir = os.path.join(os.getcwd(),'media','shp')
    print('test1')
    # folium
    lat = 55.1735998
    long = 23.8948016
    l=  -16.22
    l2= -71.59
    m = folium.Map(location=[lat,long],zoom_start=7)


    print('test2')
    ## style
    style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
    style_rivers = {'color': 'blue'}

    ## adding to view
    # folium.GeoJson(os.path.join(shp_dir, 'rivers.geojson'), name='rivers',style_function=lambda x: style_rivers).add_to(m)
    print('test3')
    folium.GeoJson(os.path.join(shp_dir, 'basin.geojson'), name='basin', style_function=lambda x: style_basin).add_to(m)
    print('test3.1')

    print('test33.2')
    folium.LayerControl().add_to(m)
    print('test33.3')


    ## exporting
    m = m._repr_html_()
    context = {'my_map': m}
    ## rendering
    print('test4')
    return render(request,'map.html',context)