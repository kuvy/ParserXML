from xml.dom import minidom

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

fwName = 'points.chp'
fw = open(fwName, 'w')
pointName = ''
pointLon = ''
pointLat = ''
typeTS = ''
lastID = 0

xmldoc = minidom.parse('stop.xml')
itemlist = xmldoc.getElementsByTagName('field')
print(len(itemlist))
# print(itemlist[0].attributes['name'].value)
for s in itemlist:
    if s.attributes['name'].value == "stop_name":
        pointName = s.childNodes[0].nodeValue
    if s.attributes['name'].value == "stop_lat":
        pointLat = s.childNodes[0].nodeValue
    if s.attributes['name'].value == "stop_long":
        pointLon = s.childNodes[0].nodeValue
    if s.attributes['name'].value == "ts_type_code":
        typeTS = s.childNodes[0].nodeValue
    if s.attributes['name'].value == "stop_id":
        stopID = s.childNodes[0].nodeValue
    if typeTS == 'b':
        if int(stopID) != lastID:
            fw.write("Name=" + pointName + "\n")
            fw.write("PExt=(" + pointLat + " " + pointLon + " R50)\n")
            fw.write("Prms=60,7\n")
            lastID = int(stopID)
print '\nComplite!'
fw.close()
exit()
