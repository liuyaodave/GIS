#! /usr/bin/env python
# -*- coding=utf-8 -*-
# @Author virqin.github.io

from lxml import etree     #将KML节点输出为字符串
import xlrd                #操作Excel
from pykml.factory import KML_ElementMaker as KML #使用factory模块

xlsfile='log.xlsx'

#加载Excel
xlsbook = xlrd.open_workbook(xlsfile)

#打开Sheet1
location = xlsbook.sheet_by_name(u'工作表1')

#取得第一和第二列全部的值
lon = location.col_values(0,0,location.nrows)
lat = location.col_values(1,0,location.nrows)

#简单判断文件中的经纬度个数是否一致
if len(lon) != len(lat):
    print 'lon != lat nums'

#使用第一个点创建Folder
fold = KML.Folder(KML.Placemark(
    KML.Point(KML.coordinates(str(lon[0]) +','+ str(lat[0]) +',0'))
    )
)

#将剩余的点追加到Folder中
for i in range(1,len(lon)):
    fold.append(KML.Placemark(
    KML.Point(KML.coordinates(str(lon[i]) +','+ str(lat[i]) +',0')))
    )

#使用etree将KML节点输出为字符串数据
content = etree.tostring(etree.ElementTree(fold),pretty_print=True)

#保存到文件，然后就可以在Google地球中打开了
with open('gen.kml', 'w') as fp:
    fp.write(content)