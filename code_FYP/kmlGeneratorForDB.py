from lxml import etree
from pykml.factory import KML_ElementMaker as KML
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client.google_ear

collection = db.test_collection


coord = KML.coordinates("-159,21\n-159,22")
lr = KML.LinearRing(coord)
ob = KML.outerBoundaryIs(lr)
am = KML.altitudeMode("clampToGround")
pg = KML.Polygon(am, ob, id="g867")
pm1 = KML.Placemark(pg)

coord2 = KML.coordinates("-999\n000")
lr2 = KML.LinearRing(coord2)
ob2 = KML.outerBoundaryIs(lr2)
am2 = KML.altitudeMode("clampToGround")
pg2 = KML.Polygon(am2, ob2, id="g867")
pm2 = KML.Placemark(pg2)

l = [pm1, pm2]

kml = KML.klm(l, xmlns="hello")

print l

print etree.tostring(kml,pm1, pm2, pretty_print=True)


s = "KML.kml(name, open, style"

placemarks = []

for i in range(len(placemarks)):
  s += ", placemarks[i]"

s += ")"

kml_result = eval(s)





