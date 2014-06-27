# coding: utf-8
# Google Map Tile File 整理工具

import re, os, shutil


for obj in os.listdir("."):
    if obj.endswith(".png"):
        tile = re.match('gm_(?P<lat>\d*?)_(?P<lng>\d*?)_(?P<zoom>\d*?)\.png', obj)
        zoom = tile.group('zoom')
        lat = tile.group('lat')
        lng = tile.group('lng')
        if not os.path.exists('./' + zoom):
            os.makedirs('./' + zoom)
        if not os.path.exists('./' + zoom + '/' + lat):
            os.makedirs('./' + zoom + '/' + lat)
        if not os.path.exists('./' + zoom + '/' + lat + '/' + lng):
            os.makedirs('./' + zoom + '/' + lat + '/' + lng)
        shutil.copy(obj, './' + zoom + '/' + lat + '/' + lng + '/')
