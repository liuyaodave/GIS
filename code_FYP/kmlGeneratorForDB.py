from pymongo import MongoClient
from lxml import etree
from pykml.factory import KML_ElementMaker as KML
import datetime

client = MongoClient('localhost', 27017)

db = client.google_eath

#print db.collection_names()

city = db.city


coord_Hawaii = city.find_one({"name": "Hawaii"})["coordinates"]


record_no = city.count()

check_point = open('check_point.txt','r')

check_point_version = check_point.read()

if int(record_no) > int(check_point_version):

	print "======== Generate New KML File ========"
	coord = KML.coordinates(coord_Hawaii)
	point = KML.Point(coord)
	descrip = KML.description("Attached to the ground.")
	name = KML.name("Simple placemark")
	placemark = KML.Placemark(name,descrip,point)
	kml = KML.kml(placemark)

	content_kml = etree.tostring(kml, pretty_print=True)

	print etree.tostring(kml, pretty_print=True)

	fo = open("placemark.kml","wb")
	fo.write(content_kml)
	fo.close()
