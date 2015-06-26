#!/usr/bin/env python

# -*- coding:utf8 -*-
 
from geopy.geocoders import Nominatim, GoogleV3, Yandex
import sys
import codecs
import json
import re
import csv

from sys import argv

if __name__=="__main__":
#  sys.stdin = codecs.getreader('utf8')(sys.stdin)
  sys.stdout = codecs.getwriter('utf8')(sys.stdout) 

  geolocator = Yandex()
  #geolocator = GoogleV3(api_key="AIzaSyDEjxgSQ6KDanVIRs2_S2BUI_PwEvIklII") #, secret_key="YVUA6X1jWYVoyS44e7y9ic9u")
  #geolocator = Nominatim()

  pairreader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
  for row in pairreader:
    id=row[0].decode('utf8')
    if int(id) % 12 != int(argv[1]) :
      continue
    
    _address=row[1].decode('utf8')
    address=re.sub(r'^"|"$',"", _address)
    address=re.sub(r'^\d+\,?\s*', '', address) 
    location = geolocator.geocode(address) #"175 5th Avenue NYC")
    #print location 
    print "%s,%f,%f,\"%s\",%s"%(id, location.latitude, location.longitude, _address, json.dumps(location.address, location.latitude, location.longitude, location.raw))
